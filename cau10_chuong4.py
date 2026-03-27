import os
import time

def clear_screen():
    # Xóa màn hình (Windows hoặc macOS/Linux)
    os.system('cls' if os.name == 'nt' else 'clear')

# Danh sách 4 hình cần hiển thị
shapes = [
    """
      * 
      * *
      * * *
* * * * * * *
* * *
* * 
*
""",
    """
      * 
      * *
      *   *
* * * * * * *
*   *
* * 
*
""",
    """
       * * * *
       * * * 
       * *
       *
     * *
   * * *
 * * * * 
""",
    """
       * * * *
       *   * 
       * *
       *
     * *
   *   *
 * * * * 
"""
]

# Lặp qua từng hình
for shape in shapes:
    clear_screen()   # Xóa màn hình
    print(shape)     # In hình ra
    time.sleep(5)    # Dừng 5 giây trước khi qua hình tiếp

print("Đã xuất hiện lần lượt tất cả các hình.")