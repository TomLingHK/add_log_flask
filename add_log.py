from datetime import datetime
import os

def add_log(app_const, dir_name, file_name, content):
    BASE_PATH = app_const['BASE_PATH']
    
    if not os.path.exists(BASE_PATH + dir_name):
        raise Exception(f"Directory {BASE_PATH + dir_name} does not exist.")
    if not os.path.isdir(BASE_PATH + dir_name):
        raise Exception(f"{BASE_PATH + dir_name} is not a directory.")
    
    file_path = BASE_PATH + dir_name + file_name
    
    ## Divide content by \n and write to file
    content_lines = content.split('\n')
    
    ## Add timestamp to each line
    timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
    content_lines = [f"{timestamp} {line}" for line in content_lines]
    
    # Create file if not exists, else append to file
    mode = 'a' if os.path.exists(file_path) else 'w'
    
    with open(file_path, mode) as f:
        for line in content_lines:
            f.write(line + "\n")
            
    lines_added = len(content_lines)
    return_msg = f"Added {lines_added} lines to {file_path}"
    
    print(f"✅ {return_msg}")
    return {"message": return_msg}
    
    
if __name__ == "__main__":
    add_log()