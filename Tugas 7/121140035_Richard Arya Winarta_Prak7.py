import tkinter as tk
import random

"""
Game snake sederhana, fitur = score point sytem ketika makan target (food), 
game over ketika collide dengan tembok

Richard 121140035
"""

area_width = 640
area_height = 640
pixel = 32

class Snake(tk.Canvas):
    def __init__(self):
        super().__init__(width=area_width, height=area_height, bg='black', highlightthickness=0)

        self.score = 2
        self.snake_body = [(128, 128), (96, 128)]
        self.food = None
        self.arah = "d"
        self.scores = [2]
        
        self.draw_menu()
    
    def draw_menu(self):
        self.delete(tk.ALL)
        self.value = tk.IntVar()
        
        self.canvas = tk.Canvas(window, width=640, height=640, bg='#f0f0f0')
        self.canvas.place(x=0, y=0)
        self.canvas.create_text(
            320,
            200,
            text=f"Game Snake",
            fill="black",
            font=("Courier", 48, 'bold'),
            anchor="s"
        )
        self.canvas.create_text(
            320,
            260,
            text=f"Hi Score : {max(self.scores)}",
            fill="red",
            font=("Courier", 15, 'bold'),
            anchor="center"
        )
        self.canvas.create_text(
            640,
            640,
            text=f"Credit : Richard - 121140035 - RB  ",
            fill="blue",
            font=("Calibri", 15),
            anchor="se"
        )
        
        self.level_easy = tk.Radiobutton(window, text='Easy Mode', variable=self.value, value=1, font=("Arial", 16), command=self.level_command)
        self.level_medium = tk.Radiobutton(window, text='Medium Mode', variable=self.value, value=2, font=("Arial", 16), command=self.level_command)
        self.level_hard = tk.Radiobutton(window, text='Hard Mode', variable=self.value, value=3, font=("Arial", 16), command=self.level_command)
        self.level_easy.place(x=320, y=320, anchor='center')
        self.level_medium.place(x=320, y=360, anchor='center')
        self.level_hard.place(x=320, y=400, anchor='center')
        
        self.play = tk.Button(window, text='Start Game', bg = 'red', fg='white', width=20, height=2, font=(14), command=self.play_command)
        self.play.place(x=320, y=480, anchor='center')
        
    
    def play_command(self):
        temp = self.value.get()
        
        #exception handling attribute error
        try:
            self.speed += 1
        except AttributeError:
            self.canvas.create_text(
                320,
                600,
                text=f"Pilih Level !!!!!",
                fill="black",
                font=("Courier", 20),
                anchor="s"
            )
            
        if temp==1 or temp==2 or temp==3:
            self.start_game()
        
    def level_command(self):
        temp = self.value.get()
        if temp==1:
            self.speed = 100
        elif temp==2:
            self.speed = 50
        elif temp==3:
            self.speed = 25
    
    def start_game(self):
        self.canvas.destroy()
        self.play.destroy()
        self.level_easy.destroy()
        self.level_medium.destroy()
        self.level_hard.destroy()
        self.bind_all("<Key>", self.key_pressed)
        self.food_loc()
        self.refresh_canvas()
        self.after(self.speed, self.game_loop)
    
    def key_pressed(self, e):
        new = e.keysym
        arahnya = ("w", "s", "a", "d")
        forbidden = ({"w", "s"}, {"a", "d"}, {"s", "w"}, {"a", "d"})
        
        if (new in arahnya) and {new, self.arah} not in forbidden :
            self.arah = new
    
    def draw_score(self):
        teks = f"Score = {self.score}"
        self.create_text(32, 32, text=teks, fill="white", font=("Arial", 32), anchor='nw')
    
    def draw_info(self):
        teks = "tombol -a- ke kiri\ntombol -d- ke kanan\ntombol -w- ke atas\ntombol -s- ke bawah"
        self.create_text(640, 0, text=teks, fill="white", font=("Arial", 16), anchor='ne')
    
    def draw_snake(self):
        for x,y in self.snake_body:
            self.create_rectangle(x, y, x+pixel, y+pixel, fill='red')
    
    def food_loc(self):
        x = random.randint(0, (area_width - pixel) / pixel) * pixel
        y = random.randint(0, (area_height - pixel) / pixel) * pixel
        self.food = (x,y)
        
    def draw_food(self):
        x,y = self.food
        self.create_oval(x, y, x+pixel, y+pixel, fill="yellow")
           
    def refresh_canvas(self):
        self.delete(tk.ALL) #refresh canvas baru
        self.draw_info()
        self.draw_score()
        self.draw_food()
        self.draw_snake()
        
    def game_loop(self):
        if self.cek_posisi():
            self.game_over()
            return
        
        self.cek_food()
        self.snake_movement()
        self.after(self.speed, self.game_loop)
        
    def cek_food(self):
        if self.food == None:
            return
        
        if(self.snake_body[0] == self.food):
            self.score += 1
            self.snake_body.append((0, 0))
            self.food_loc()
            
    def cek_posisi(self):
        head_x, head_y = self.snake_body[0]
        
        return (
            head_x < 0 or
            head_x >= area_width or
            head_y < 0 or
            head_y >= area_height or
            (head_x, head_y) in self.snake_body[1:]
        )
        
    def snake_movement(self):
        head_x, head_y = self.snake_body[0]
        
        if self.arah == "d":
            new_head = (head_x + pixel, head_y)
        elif self.arah == "a":
            new_head = (head_x - pixel, head_y)
        elif self.arah == "w":
            new_head = (head_x, head_y - pixel)
        elif self.arah == "s":
            new_head = (head_x, head_y + pixel)

        self.snake_body = [new_head] + self.snake_body[:-1]
        
        self.refresh_canvas()
        
    def game_over(self):
        global running
        
        self.delete(tk.ALL)
        self.create_text(
            self.winfo_width() / 2,
            self.winfo_height() / 2 - 50,
            text=f"Game over! You scored {self.score} points.",
            fill="white",
            font=("Arial", 16),
            anchor="center"
        )
        self.scores.append(self.score)
        self.restart = tk.Button(window, width=10, height=1, bg='red', anchor='center', text='Restart', font=("Arial", 16), fg='white', command=self.button_restart)
        self.restart.place(anchor='center', x=320, y=320)
       
    def button_restart(self):
        self.restart.destroy()
        self.score = 2
        delattr(self, 'speed')
        self.snake_body = [(128, 128), (96, 128)]
        self.food = None
        self.arah = "d"
        self.draw_menu()
        
window = tk.Tk()
window.title("Snake")
window.resizable(False, False)

game = Snake()
game.pack()

window.mainloop()