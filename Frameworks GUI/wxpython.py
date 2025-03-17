import wx

class MyApp(wx.App):
    def OnInit(self):
        frame = wx.Frame(None, title="Exemplo wxPython")
        panel = wx.Panel(frame)

        # Criação do layout
        sizer = wx.BoxSizer(wx.VERTICAL)

        # Criação de um rótulo
        label = wx.StaticText(panel, label="Olá, wxPython!")
        sizer.Add(label, 0, wx.ALL | wx.CENTER, 5)

        # Criação de um botão
        button = wx.Button(panel, label="Clique em mim")
        button.Bind(wx.EVT_BUTTON, self.on_button_click)
        sizer.Add(button, 0, wx.ALL | wx.CENTER, 5)

        panel.SetSizer(sizer)
        frame.Show()
        return True

    def on_button_click(self, event):
        print("Botão clicado!")

if _name_ == "_main_":
    app = MyApp()
    app.MainLoop()