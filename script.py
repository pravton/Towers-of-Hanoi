
from stack import Stack
import tkinter as tk
from tkinter import messagebox

class TowersOfHanoi:
    def __init__(self, num_disks):
        self.num_disks = num_disks
        self.num_optimal_moves = (2 ** num_disks) - 1
        self.num_user_moves = 0
        self.stacks = []
        self.left_stack = Stack('Left')
        self.stacks.append(self.left_stack)
        self.middle_stack = Stack('Middle')
        self.stacks.append(self.middle_stack)
        self.right_stack = Stack('Right')
        self.stacks.append(self.right_stack)
        self.canvas = None  # Initialize canvas attribute

    def setup_game(self):
        for i in range(self.num_disks):
            self.left_stack.push(i)

    def move_disk(self, from_stack, to_stack):
        if from_stack.is_empty():
            messagebox.showerror("Invalid Move", "Source stack is empty!")
        elif to_stack.is_empty() or from_stack.peek() < to_stack.peek():
            disk = from_stack.pop()
            to_stack.push(disk)
            self.num_user_moves += 1
            self.check_game_over()
            if self.canvas:  # Update display only if canvas is created
                self.update_display()
        else:
            messagebox.showerror("Invalid Move", "Cannot place a larger disk on top of a smaller disk!")

    def check_game_over(self):
        if self.right_stack.get_size() == self.num_disks:
            messagebox.showinfo("Game Over", f"You completed the game in {self.num_user_moves} moves. Optimal moves: {self.num_optimal_moves}")
            self.reset_game()

    def reset_game(self):
        self.left_stack.clear()
        self.middle_stack.clear()
        self.right_stack.clear()
        self.num_user_moves = 0
        self.setup_game()

    def update_display(self):
        # Clear previous canvas drawings
        self.canvas.delete("disk")
        for i, stack in enumerate(self.stacks):
            x_center = 150 + i * 150
            for j, disk_size in enumerate(stack.get_all_items()):
                self.canvas.create_rectangle(x_center - disk_size * 10, 350 - j * 20, x_center + disk_size * 10, 370 - j * 20, fill="blue", tags="disk")

    def play(self):
        root = tk.Tk()
        root.title("Towers of Hanoi")

        self.canvas = tk.Canvas(root, width=800, height=400)
        self.canvas.pack()
        self.setup_game()  # Setup the game after canvas creation

        def on_from_stack_selected(from_stack_idx):
            from_stack = self.stacks[from_stack_idx]
            to_stack_idx = (from_stack_idx + 1) % 3
            to_stack = self.stacks[to_stack_idx]
            self.move_disk(from_stack, to_stack)

        tk.Button(root, text="Move Disk Left to Middle", command=lambda: on_from_stack_selected(0)).pack()
        tk.Button(root, text="Move Disk Middle to Right", command=lambda: on_from_stack_selected(1)).pack()
        tk.Button(root, text="Move Disk Right to Left", command=lambda: on_from_stack_selected(2)).pack()
        tk.Button(root, text="Reset Game", command=self.reset_game).pack()

        self.update_display()
        root.mainloop()

if __name__ == "__main__":
    try:
        num_disks = int(input("How many disks do you want to play with? (3 or more): "))
        if num_disks < 3:
            raise ValueError("Number of disks must be 3 or more.")
        game = TowersOfHanoi(num_disks)
        game.play()
    except ValueError as e:
        print("Invalid input:", e)
