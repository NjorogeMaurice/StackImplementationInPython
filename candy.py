from tkinter import BOTTOM, TOP, Button, Canvas, RAISED, Tk
from tkinter.messagebox import showerror, showinfo

#Array-based stack implementation of a candy dispenser
class Candy_Dispenser:

  def __init__(self, window: Tk):
    self.window = window
    self.color_primary = "green"

    self.candy_stack = []
    self.max_size = 12

    # Spring
    self.spring_left = 75
    self.spring_right = 287
    self.spring_top = 120
    self.spring_bottom = 600
    self.spring_offset = 30  # Distance moved by spring
    self.spring_thickness = 1
    
    # New candy bar
    self.new_bar_bottom = self.spring_top + 35 # Candy height = 56px.
    self.new_bar_cx = (self.spring_left + self.spring_right) / 2  # Center X
    self.new_bar_cy = (self.spring_top + self.new_bar_bottom) / 2  # Center Y

    self.a_y=120
    self.b_y=215
    self.c_y=310
    self.d_y=405
    self.e_y=500

    ##Top panel consists of the candy dispenser, spring, candy
    self.top_panel = Canvas(self.window, width=(window_width/2), height=(window_height/2))
    self.top_panel.pack(side=TOP)
    
    
    ##Bottom panel consists of buttons. push, pop, isEmpty, size, top
    self.bottom_panel = Canvas(self.window, width=(window_width/2), height=(window_height/2))
    self.bottom_panel.pack(side=BOTTOM)

    ###Drawing the spring
    self.a = self.top_panel.create_line(self.spring_left, self.a_y, self.spring_right, self.a_y, 
                                         width=self.spring_thickness, smooth=True)
    
    self.a_b1 = self.top_panel.create_line(self.spring_left, self.a_y, self.spring_right, self.b_y,
                                          width=self.spring_thickness, smooth=True)
    
    self.a_b2 = self.top_panel.create_line(self.spring_left, self.b_y, self.spring_right, self.a_y, 
                                           width=self.spring_thickness, smooth=True)
    
    self.b = self.top_panel.create_line(self.spring_left, self.b_y, self.spring_right, self.b_y, 
                                         width=self.spring_thickness, smooth=True)
    
    self.b_c1 = self.top_panel.create_line(self.spring_left, self.c_y, self.spring_right, self.b_y, 
                                           width=self.spring_thickness, smooth=True)
    
    self.b_c2 = self.top_panel.create_line(self.spring_right, self.c_y, self.spring_left, self.b_y, 
                                           width=self.spring_thickness, smooth=True)
    
    self.c = self.top_panel.create_line(self.spring_left, self.c_y, self.spring_right, self.c_y, 
                                         width=self.spring_thickness, smooth=True)
    
    self.c_d1 = self.top_panel.create_line(self.spring_left, self.c_y, self.spring_right, self.d_y,
                                            width=self.spring_thickness, smooth=True)
    
    self.c_d2 = self.top_panel.create_line(self.spring_right, self.c_y, self.spring_left, self.d_y,
                                            width=self.spring_thickness, smooth=True)
    
    self.d = self.top_panel.create_line(self.spring_left, self.d_y, self.spring_right, self.d_y, 
                                         width=self.spring_thickness, smooth=True)
    
    self.d_e1 = self.top_panel.create_line(self.spring_left, self.d_y, self.spring_right, self.e_y,
                                            width=self.spring_thickness, smooth=True)
    
    self.d_e2 = self.top_panel.create_line(self.spring_right, self.d_y, self.spring_left, self.e_y,
                                            width=self.spring_thickness, smooth=True)
    
    self.top_panel.create_line(self.spring_left, self.e_y, self.spring_right, self.e_y, 
                                width=self.spring_thickness, smooth=True)
    
    self.top_panel.create_line(70,70,70,540, width=3)
    self.top_panel.create_line(290,70,290,540, width=3)
    self.top_panel.create_line(290,540,70,540, width=3)
    
    ####Drawing the buttons
    
    ##push() button
    Button(self.bottom_panel, text="Push", fg="white", bg=self.color_primary, font=("Arial", 14, "italic"),
           relief=RAISED,bd=7,command=self.push).place(x=0, y=100)
    
    ##pop() button
    Button(self.bottom_panel, text="Pop", fg="white", bg=self.color_primary, font=("Arial", 14, "italic"),
           relief=RAISED,bd=7,command=self.pop).place(x=85, y=100)
    

    ##top() button
    Button(self.bottom_panel, text="Top", fg="white", bg=self.color_primary, font=("Arial", 14, "italic"),
           relief=RAISED,bd=7,command=self.top).place(x=165, y=100)

    
    ##size() button
    Button(self.bottom_panel, text="Size", fg="white", bg=self.color_primary, font=("Arial", 14, "italic"),
           relief=RAISED,bd=7,command=self.report_size).place(x=240, y=100)
    

    ##isEmpty() button
    Button(self.bottom_panel, text="IsEmpty", fg="white", bg=self.color_primary,font=("Arial", 14, "italic"),
           relief=RAISED,bd=7,command=self.report_empty_stat).place(x=320, y=100)
    

  ## pop() method    
  def pop(self):

    ##Checks if the stack is empty
    if self.size() > 0:
      
      ##if not, the top most candy is popped 
      candy = self.candy_stack.pop()
      self.top_panel.delete(candy['bar'])
      self.top_panel.delete(candy['label'])
      

      ##The springs are updated
      self.update_dispenser('pop')
    else:

      ##if it's empty, it return an error since there is no top element
      showerror("Error","The Candy Dispenser is empty.")


  ## push() method
  def push(self):

    ## Checks if the stack is full
    if self.size() < self.max_size:
      ##if not, a new candy is appended
      self.candy_stack.append(self.draw_candy())  # Add candy to stack.
      
      ##The springs are updated
      self.update_dispenser('push')

    else:

      ##if it is empty, an error is returned
      showerror("Error", "The Candy Dispenser is full.")
  

  ### method to draw a candy
  def draw_candy(self):
    
    bar = self.top_panel.create_rectangle(self.spring_left, self.spring_top, self.spring_right, 
                                      self.new_bar_bottom,fill="orange")
    tag = f'Candy {self.size() + 1}'
    label = self.top_panel.create_text(self.new_bar_cx, self.new_bar_cy, text=tag, fill='white')
    return { 'bar': bar, 'label': label, 'tag': tag}


  ## method to update the springs during pop and push methods
  def update_dispenser(self, mode):

    # Update position of all candies excluding the topmost in the stack.
    # When the method is push()
    if mode == 'push':
      ## every candy existing in the stack is updated
      for i in range(self.size()):
        self.update_candy_pos(self.candy_stack[i], (self.size() - 1) - i)
        
      # Update spring's pitch.
      self.a_y += self.spring_offset 
      self.b_y += self.spring_offset /1.5
      self.c_y += self.spring_offset / 2
      self.d_y += self.spring_offset / 3

    ## when method is pop()  
    elif mode == 'pop':
      stack_size = self.size()
      ## every candy existing in the stack is updated
      for i in range(stack_size):
        self.update_candy_pos(self.candy_stack[i], stack_size - (i + 1))

      # Update spring's pitch.
      self.a_y -= self.spring_offset
      self.b_y -= self.spring_offset / 1.5
      self.c_y -= self.spring_offset / 2
      self.d_y -= self.spring_offset / 3
    else:
      raise Exception

    # Update the springs.
    self.top_panel.coords(self.a, self.spring_left, self.a_y, self.spring_right, self.a_y)
    self.top_panel.coords(self.a_b1, self.spring_left, self.a_y, self.spring_right, self.b_y)
    self.top_panel.coords(self.a_b2, self.spring_left, self.b_y, self.spring_right, self.a_y)
    self.top_panel.coords(self.b, self.spring_left, self.b_y, self.spring_right, self.b_y)
    self.top_panel.coords(self.b_c1, self.spring_left, self.c_y, self.spring_right, self.b_y)
    self.top_panel.coords(self.b_c2, self.spring_right, self.c_y, self.spring_left, self.b_y)
    self.top_panel.coords(self.c, self.spring_left, self.c_y, self.spring_right, self.c_y)
    self.top_panel.coords(self.c_d1, self.spring_left, self.c_y, self.spring_right, self.d_y)
    self.top_panel.coords(self.c_d2, self.spring_right, self.c_y, self.spring_left, self.d_y)
    self.top_panel.coords(self.d, self.spring_left, self.d_y, self.spring_right, self.d_y)
    self.top_panel.coords(self.d_e1, self.spring_left, self.d_y, self.spring_right, self.e_y)
    self.top_panel.coords(self.d_e2, self.spring_right, self.d_y, self.spring_left, self.e_y)
    
    
    self.top_panel.update()  # Redrawing the components

  def update_candy_pos(self, candy, y):
    updated_bar_top = self.spring_top + (self.spring_offset * y)
    updated_bar_bottom = self.new_bar_bottom + (self.spring_offset * y)

    self.top_panel.coords(
      candy['bar'], self.spring_left, updated_bar_top, self.spring_right, updated_bar_bottom
    )
    self.top_panel.coords(
      candy['label'], self.new_bar_cx, (updated_bar_top + updated_bar_bottom) / 2
    )

  def size(self):
    return len(self.candy_stack)

  def report_size(self):
    showinfo('size()', f'The Candy dispenser size is {self.size()}')

  def top(self):
    if self.is_empty():
      showerror('No Top Error', 'The Candy dispenser is empty')
    else:
      showinfo('top()', f'The Top candy is "{self.candy_stack[-1]["tag"]}"')

  def is_empty(self):
    if self.size() == 0:
      return True
    return False

  def report_empty_stat(self):
    msg = 'False'
    if self.is_empty():
      msg = 'True'
    showinfo('IsEmpty()', msg)


if __name__ == '__main__':
  window_height = 1000
  window_width = 850

  root = Tk()
  root.title('Array based implementation of Candy Dispenser in Python')
  root.maxsize(window_width, window_height)
  root.minsize(window_width, window_height)
  Candy_Dispenser(root)
  root.mainloop()