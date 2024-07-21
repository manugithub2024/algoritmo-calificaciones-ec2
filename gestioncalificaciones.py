import tkinter as tk

class CalificacionesAlumnos:

    def __init__(self, root):
        self.root = root
        self.root.title('Calificación Alumnos')
        self.root.geometry('350x550')

        self.nombre_label = tk.Label(root, text="Nombres :")
        self.nombre_label.pack(pady=5)
        self.nombre_entry = tk.Entry(root)
        self.nombre_entry.pack(pady=5)

        self.calificacion1_label = tk.Label(root, text="Nota 1:")
        self.calificacion1_label.pack(pady=5)
        self.calificacion1_entry = tk.Entry(root)
        self.calificacion1_entry.pack(pady=5)

        self.calificacion2_label = tk.Label(root, text="Nota 2:")
        self.calificacion2_label.pack(pady=5)
        self.calificacion2_entry = tk.Entry(root)
        self.calificacion2_entry.pack(pady=5)

        self.calificacion3_label = tk.Label(root, text="Nota 3:")
        self.calificacion3_label.pack(pady=5)
        self.calificacion3_entry = tk.Entry(root)
        self.calificacion3_entry.pack(pady=5)

        self.calificacion4_label = tk.Label(root, text="Nota 4:")
        self.calificacion4_label.pack(pady=5)
        self.calificacion4_entry = tk.Entry(root)
        self.calificacion4_entry.pack(pady=5)

        self.calcular_button = tk.Button(root, text="Calcular promedio y guardar", bg="gray", fg="black", font=("arial",10), command=self.calcular_promedio)                      
        self.calcular_button.pack(pady=10)

        self.mostrar_button = tk.Button(root, text="Mostrar resultados", bg="gray", fg="black", font=("arial",10), command=self.mostrar_resultados)
        self.mostrar_button.pack(pady=10)
        
        self.lista_alumnos_text = tk.Text(root)
        self.lista_alumnos_text.pack()
        self.lista_alumnos_text.place(x=0, y=400)

    def calcular_promedio(self):
        nombre = self.nombre_entry.get()
        calificacion1 = float(self.calificacion1_entry.get())
        calificacion2 = float(self.calificacion2_entry.get())
        calificacion3 = float(self.calificacion3_entry.get())
        calificacion4 = float(self.calificacion4_entry.get())

        promedio = (calificacion1 + calificacion2 + calificacion3 + calificacion4) / 4

        with open("alumnos.txt", "a") as archivo:
            archivo.write(f"{nombre}: {calificacion1}/{calificacion2}/{calificacion3}/{calificacion4} promedio final: {promedio}\n")
        self.lista_alumnos_text.insert(tk.END, f"{nombre}: {calificacion1}/{calificacion2}/{calificacion3}/{calificacion4} promedio final: {promedio}\n")
                            
    def mostrar_resultados(self):
        self.lista_alumnos_text.delete(1.0, tk.END)
        with open("alumnos.txt", "r") as archivo:
            for linea in archivo:
                self.lista_alumnos_text.insert(tk.END, linea)

root = tk.Tk()
app = CalificacionesAlumnos(root)
root.mainloop()

