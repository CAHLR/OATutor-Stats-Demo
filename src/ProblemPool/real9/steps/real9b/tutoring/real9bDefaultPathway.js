var hints = [{id: "real9b-h1", type: "hint", dependencies: [], title: "Substitute", text: "Plug in 10 for t. You get the equation $$\\frac{10}{\\left(2\\right) \\left(10\\right)-\\left(1\\right)}$$"}, {id: "real9b-h2", type: "scaffold", problemType: "TextBox", answerType: "arithmetic", hintAnswer: ["20"], dependencies: ["real9b-h1"], title: "Multiplication", text: "What is 2*10?"}, {id: "real9b-h3", type: "scaffold", problemType: "TextBox", answerType: "arithmetic", hintAnswer: ["19"], dependencies: ["real9b-h2"], title: "Subtraction", text: "What is 20-1"}, {id: "real9b-h4", type: "scaffold", problemType: "TextBox", answerType: "arithmetic", hintAnswer: ["10/19"], dependencies: ["real9b-h3"], title: "Substitute", text: "What is 10/(2(10)-1)?"}, ]; export {hints};