from dataclasses import dataclass
@dataclass
class Student:
    name: str
    age: str
    sid: str

    def to_line(self):
        return f"{self.name}|{self.age}|{self.sid}\n"

    @classmethod
    def from_line(cls, line):
        parts = line.strip().split("|")
        if len(parts) != 3:
            raise ValueError("invalid line")
        return cls(parts[0], parts[1], parts[2])


class StudentManager:
    def __init__(self, filename):
        self.filename = filename
        self._ensure_file()

    def _ensure_file(self):
        open(self.filename, "a", encoding="utf-8").close()

    def get_all(self):
        students = []
        with open(self.filename, "r", encoding="utf-8") as f:
            for line in f:
                if line.strip() == "":
                    continue
                try:
                    students.append(Student.from_line(line))
                except ValueError:
                    continue
        return students

    def add(self, name, age, sid):
        student = Student(name, age, sid)
        with open(self.filename, "a", encoding="utf-8") as f:
            f.write(student.to_line())

    def search(self, q):
        return [
            s for s in self.get_all()
            if q == s.name or q == s.sid
        ]

    def find_by_sid(self, sid):
        for s in self.get_all():
            if s.sid == sid:
                return s
        return None

    def delete(self, sid):
        students = self.get_all()
        new_students = [s for s in students if s.sid !=sid]
        deleted = len(new_students) != len(students)
        self._write_all(new_students)
        return deleted

    def edit(self, sid, new_name, new_age, new_sid):
        students = self.get_all()
        edited = False

        for s in students:
            if s.sid == sid:
                s.name = new_name
                s.age = new_age
                s.sid = new_sid
                edited = True

        self._write_all(students)
        return edited

    def _write_all(self, students):
        with open(self.filename, "w", encoding="utf-8") as f:
            for s in students:
                f.write(s.to_line())
class StudentApp:
    def __init__(self, filename="students2.txt"):
        self.manager = StudentManager(filename)

    def run(self):
        while True:
            self._show_menu()
            choice = input("choose a number : ")

            if choice == "1":
                self._add_student()
            elif choice == "2":
                self._search_student()
            elif choice == "3":
                self._display_students()
            elif choice == "4":
                self._delete_student()
            elif choice == "5":
                self._edit_student()
            elif choice == "6":
                print("goodbye")
                break
            else:
                print("please enter the correct number.")
    def _show_menu(self):
        print("\n--- student menu ---")
        print("1. add std")
        print("2. search std ")
        print("3. display std ")
        print("4. delete std")
        print("5. edit std")
        print("6. exit ")

    def _add_student(self):
        name = input("name: ")
        age = input("age: ")
        sid = input("std_id: ")
        self.manager.add(name, age, sid)
        print("student added.")

    def _search_student(self):
        q = input("name or std_id: ")
        results = self.manager.search(q)

        if not results:
            print("not found")
        else:
            for s in results:
                print(f"name: {s.name} | age: {s.age} | id: {s.sid}")

    def _display_students(self):
        students = self.manager.get_all()

        if not students:
            print("the list is empty.")
        else:
            for s in students:
                print(f"name: {s.name} | age: {s.age} | id: {s.sid}")

    def _delete_student(self):
        sid = input("std_id for delete ")

        if self.manager.delete(sid):
            print("deletion completed")
        else:
            print("not found")

    def _edit_student(self):
        sid = input("std_id for edit:")

        if self.manager.find_by_sid(sid) is None:
            print("not found")
            return

        new_name = input("new name: ")
        new_age = input("new age: ")
        new_sid = input("new id: ")

        self.manager.edit(sid, new_name, new_age, new_sid)
        print("the edit has been made.")


if __name__ == "__main__":
    app = StudentApp()
    app.run()