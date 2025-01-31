class SolveButton:
    def __init__(self, body):
        self.body = body

    def set_loading(self):
        """
        Disables the button for processing.
        """

        self.body.setText("Processing...")
        self.body.setProperty("is_disabled", "true")
        self.render_button()

    def set_finished(self):
        """
        Enables the button after processing finishes.
        """

        self.body.setText("Solve")
        self.body.setProperty("is_disabled", "false")
        self.render_button()

    def disable(self, is_disabled):
        """
        Disables the button for input error.
        """

        self.body.setProperty("is_disabled", is_disabled)
        self.render_button()

    def render_button(self):
        """
        Updates the button render.
        """
        
        self.body.style().unpolish(self.body)
        self.body.style().polish(self.body)
        self.body.update()
