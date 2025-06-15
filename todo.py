import json

# تحميل المهام من ملف
def load_tasks():
    try:
        with open("tasks.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

# حفظ المهام في ملف
def save_tasks(tasks):
    with open("tasks.json", "w", encoding="utf-8") as f:
        json.dump(tasks, f, ensure_ascii=False, indent=2)

tasks = load_tasks()

while True:
    print("\n--- قائمة المهام ---")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")

    print("\n1. إضافة مهمة")
    print("2. حذف مهمة")
    print("3. خروج")

    choice = input("اختار رقم العملية: ")

    if choice == "1":
        new_task = input("اكتب المهمة الجديدة: ")
        tasks.append(new_task)
        save_tasks(tasks)
        print("✅ تمت الإضافة.")
    elif choice == "2":
        task_num = int(input("اكتب رقم المهمة اللي عايز تحذفها: "))
        if 0 < task_num <= len(tasks):
            removed = tasks.pop(task_num - 1)
            save_tasks(tasks)
            print(f"❌ تم حذف: {removed}")
        else:
            print("❗ رقم غير صحيح.")
    elif choice == "3":
        print("👋 مع السلامة!")
        break
    else:
        print("❗ اختيار غير صحيح.")
