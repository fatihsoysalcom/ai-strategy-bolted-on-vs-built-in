class Task:
    """
    Görevleri temsil eden temel sınıf.
    'manual_priority' bolted-on yaklaşım için, 'ai_priority' built-in yaklaşım için kullanılır.
    """
    def __init__(self, description, deadline=None, manual_priority=None):
        self.description = description
        self.deadline = deadline
        self.manual_priority = manual_priority  # 'Bolted-On' için manuel olarak belirlenen öncelik
        self.ai_priority = None                 # 'Built-In' için YZ tarafından belirlenen öncelik
        self.is_completed = False

    def __repr__(self):
        status = " (Completed)" if self.is_completed else ""
        priority_info = ""
        if self.manual_priority is not None:
            priority_info += f" | Manual Priority: {self.manual_priority}"
        if self.ai_priority is not None:
            priority_info += f" | AI Priority: {self.ai_priority}"

        return f"Task: '{self.description}' | Deadline: {self.deadline or 'N/A'}{priority_info}{status}"


# --- Bolted-On AI Approach (Eklemek) ---
class AIBoltedOnSuggester:
    """
    Harici bir bileşen gibi eklenen Yapay Zeka önerici.
    Görev listesini alır ve bir öneri sunar.
    Ana görev yöneticisi bu olmadan da çalışır.
    """
    def suggest_next_task(self, tasks):
        active_tasks = [t for t in tasks if not t.is_completed]
        if not active_tasks:
            return "No active tasks to suggest."
        # Basit bir AI mantığı: en yüksek öncelikli veya en yakın deadline'lı görevi öner
        # Bu AI mantığı, TaskManager'ın çekirdek işlevselliğine entegre değildir.
        # Sadece bir 'eklenti'dir.
        active_tasks.sort(key=lambda t: (t.manual_priority or 999, t.deadline or "9999-12-31"))
        return f"Suggested next (Bolted-On): {active_tasks[0].description}"


class TaskManagerBoltedOn:
    """
    Yapay Zeka'nın harici bir eklenti olarak kullanıldığı görev yöneticisi.
    Temel işlevsellik YZ olmadan da tamamen çalışır.
    """
    def __init__(self):
        self.tasks = []
        self.ai_suggester = AIBoltedOnSuggester()  # YZ isteğe bağlı, harici bir bileşendir

    def add_task(self, description, deadline=None, priority=None):
        task = Task(description, deadline, manual_priority=priority)
        self.tasks.append(task)
        print(f"Added task (Bolted-On): {description}")

    def list_tasks(self):
        print("\n--- Bolted-On Task List ---")
        if not self.tasks:
            print("No tasks.")
            return
        # Çekirdek listeleme işlevselliği YZ'ye bağlı değildir.
        for task in self.tasks:
            print(task)

    def get_ai_suggestion(self):
        # YZ önerisi almak, çekirdek işlevselliğin bir parçası değil, ek bir özelliktir.
        return self.ai_suggester.suggest_next_task(self.tasks)


# --- Built-In AI Approach (İnşa Etmek) ---
class TaskManagerBuiltIn:
    """
    Yapay Zeka'nın iş süreçlerinin temel bir parçası olarak inşa edildiği görev yöneticisi.
    YZ, görevlerin yönetilme ve sunulma şeklini doğrudan etkiler.
    """
    def __init__(self):
        self.tasks = []
        self.ai_enabled = True  # YZ'nin sistemin ayrılmaz bir parçası olduğunu simüle eder

    def _determine_ai_priority(self, task):
        """
        YZ destekli önceliklendirme mantığı.
        Bu, görevin temel bir özelliğini belirler ve 'inşa edilmiş' bir parçadır.
        """
        if not self.ai_enabled:
            # YZ devre dışı bırakılırsa, temel işlevini (öncelik belirleme) sağlayamaz.
            # Bu, YZ arızasının/devre dışı bırakılmasının çekirdek mantık üzerindeki etkisini gösterir.
            return None  # YZ öncelik belirleyemez

        # Basit AI mantığı: 'urgent' içerenleri yüksek öncelikli yap
        # Gerçek bir sistemde bu daha karmaşık bir model olurdu.
        if "urgent" in task.description.lower():
            return 1  # En yüksek öncelik
        elif task.deadline and task.deadline < "2024-12-31":  # Örnek bir son tarih kontrolü
            return 2
        else:
            return 3  # Daha düşük öncelik

    def add_task(self, description, deadline=None):
        task = Task(description, deadline)
        # Görev eklenirken YZ tarafından öncelik belirlenir.
        # Bu, görevin temel bir özelliğidir.
        task.ai_priority = self._determine_ai_priority(task)  # YZ başlangıç önceliğini belirler
        print(f"Added task (Built-In, AI Priority: {task.ai_priority}): {description}")
        self.tasks.append(task)

    def list_tasks(self):
        print("\n--- Built-In Task List (AI-Sorted) ---")
        if not self.tasks:
            print("No tasks.")
            return

        if self.ai_enabled:
            # YZ tarafından belirlenen önceliklere göre sıralama,
            # listeleyici işlevselliğinin çekirdek bir parçasıdır.
            sorted_tasks = sorted(self.tasks, key=lambda t: t.ai_priority if t.ai_priority is not None else 999)
            for task in sorted_tasks:
                print(f"Task: '{task.description}' | AI Priority: {task.ai_priority or 'N/A'} | Deadline: {task.deadline or 'N/A'}")
        else:
            # YZ devre dışı: çekirdek listeleme işlevselliği bozulur.
            print("AI is disabled. Cannot sort by AI priority. Displaying in order of addition.")
            for task in self.tasks:
                print(f"Task: '{task.description}' | AI Priority: {task.ai_priority or 'N/A'} | Deadline: {task.deadline or 'N/A'}")


# --- Demonstration ---
if __name__ == "__main__":
    print("--- Demonstrating 'Bolted-On' AI (Eklemek) ---")
    bolted_on_manager = TaskManagerBoltedOn()
    bolted_on_manager.add_task("Buy groceries", "2024-11-01", 3)
    bolted_on_manager.add_task("Prepare presentation", "2024-10-25", 1)
    bolted_on_manager.add_task("Call client", "2024-10-20", 2)
    bolted_on_manager.list_tasks()
    # YZ bir eklenti özelliğidir. Çekirdek görev listesi varlığından veya yokluğundan etkilenmez.
    print(f"Bolted-On AI Suggestion: {bolted_on_manager.get_ai_suggestion()}")

    print("\n--- Demonstrating 'Built-In' AI (İnşa Etmek) ---")
    built_in_manager = TaskManagerBuiltIn()
    # YZ, görev eklenirken önceliği belirler. Bu, görevlerin nasıl yönetildiğinin ayrılmaz bir parçasıdır.
    built_in_manager.add_task("Review urgent project proposal", "2024-10-18")  # YZ öncelik 1'i belirleyecek
    built_in_manager.add_task("Schedule team meeting", "2024-10-28")  # YZ öncelik 2'yi belirleyecek
    built_in_manager.add_task("Draft blog post", "2025-01-15")  # YZ öncelik 3'ü belirleyecek
    # Liste doğal olarak YZ önceliğine göre sıralanır ve derin entegrasyonu gösterir.
    built_in_manager.list_tasks()

    print("\n--- Simulating AI Failure/Disabling in 'Built-In' System ---")
    built_in_manager.ai_enabled = False  # YZ ayrılmaz bir parçadır, devre dışı bırakılması çekirdek işlevselliği etkiler
    # YZ devre dışı bırakıldığında, temel işlevini (öncelik belirleme) sağlayamaz.
    built_in_manager.add_task("Fix critical bug urgent", "2024-10-17")  # YZ önceliği doğru ayarlayamaz (None olacak)
    # Liste artık YZ önceliğine göre sıralanmaz, bu da bozulmuş çekirdek işlevselliği gösterir.
    built_in_manager.list_tasks()
