
# 🖋️ File Read & Write Challenge with Error Handling 🧪

This Python program performs the following tasks:

### ✅ Features
1. **Reads** the content of a user-specified text file.
2. **Modifies** the content (by converting it to **uppercase**).
3. **Writes** the modified content into a **new file**.
4. Includes proper **error handling** to manage missing or unreadable files.

---

### 📁 How It Works

1. The program prompts the user to enter the filename (e.g., `example.txt`).
2. It attempts to open and read the file.
3. If the file is found:
   - The content is read.
   - It is transformed (converted to uppercase).
   - A new file is created with the name `modified_<original_filename>`.
4. If the file is **not found** or **can't be read**, an error message is displayed.

---

### 🧪 Example Usage

```bash
$ python file_modifier.py
Enter the name of the file to read: mynotes.txt
Modified content written to 'modified_mynotes.txt' successfully.
