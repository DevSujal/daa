vba_code = """
Sub CreateGameOfLifePresentation()
    Dim slideIndex As Integer
    
    ' Create a new PowerPoint application
    Dim pptApp As Object
    Set pptApp = CreateObject("PowerPoint.Application")
    pptApp.Visible = True
    
    ' Create a new presentation
    Dim pptPresentation As Object
    Set pptPresentation = pptApp.Presentations.Add
    
    ' Slide 1: Introduction
    slideIndex = slideIndex + 1
    Call AddSlide(pptPresentation, slideIndex, "Introduction", "Game of Life Simulation", "Briefly introduce the Game of Life, its origin, and the problem definition. Mention that the code aims to simulate the next state of the board based on specific rules.")
    
    ' Slide 2: Problem Overview
    slideIndex = slideIndex + 1
    Call AddSlide(pptPresentation, slideIndex, "Problem Overview", "Rules of the Game", "Summarize the rules as stated in the Wikipedia article. Emphasize the four rules that govern the state transitions: under-population, survival, over-population, and reproduction.")
    
    ' Slide 3: Code Structure
    slideIndex = slideIndex + 1
    Call AddSlide(pptPresentation, slideIndex, "Code Structure", "Counting Neighbors", "Introduce the `count_neighbors` function, explaining its purpose in counting live neighbors for a given cell. Highlight the boundary checks and the conditions for counting live neighbors.")
    
    ' Slide 4: Code Structure (Contd)
    slideIndex = slideIndex + 1
    Call AddSlide(pptPresentation, slideIndex, "Code Structure (Contd)", "Updating the Board", "Explain the logic behind updating the board in the `game_of_life` function. Describe how the rules are applied to each cell and how the new state is determined based on the neighbor count.")
    
    ' Slide 5: Example Board
    slideIndex = slideIndex + 1
    Call AddSlide(pptPresentation, slideIndex, "Example Board", "Initial and Final Board State", "Display the initial state of the board and discuss the representation (0 for dead, 1 for live). After running the `game_of_life` function, show the final state of the board.")
    
    ' Slide 6: Implementation Details
    slideIndex = slideIndex + 1
    Call AddSlide(pptPresentation, slideIndex, "Implementation Details", "Implementation Choices", "Discuss any specific implementation choices made in the code. Address any notable decisions, optimizations, or considerations made during the development.")
    
    ' Slide 7: Conclusion
    slideIndex = slideIndex + 1
    Call AddSlide(pptPresentation, slideIndex, "Conclusion", "Conclusion and Takeaways", "Summarize the key points of the presentation. Discuss the significance of the Game of Life simulation and how it can be applied or extended. Invite questions and discussions from the audience.")
End Sub

Sub AddSlide(pptPresentation As Object, slideIndex As Integer, title As String, subtitle As String, content As String)
    ' Add a new slide to the presentation
    Dim slideObject As Object
    Set slideObject = pptPresentation.Slides.Add(slideIndex, ppLayoutText)
    
    ' Set slide title
    slideObject.Shapes(1).TextFrame.TextRange.Text = title
    
    ' Set slide subtitle
    slideObject.Shapes(2).TextFrame.TextRange.Text = subtitle
    
    ' Set slide content
    slideObject.Shapes(3).TextFrame.TextRange.Text = content
End Sub
"""

# Print or copy the generated VBA code to use in PowerPoint
print(vba_code)
