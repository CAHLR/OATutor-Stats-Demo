var hints = [{id: "SubAdd1a-h1", type: "hint", dependencies: [], title: "Substitution", text: "Substitute the number in for the variable in the equation."}, {id: "SubAdd1a-h2", type: "hint", dependencies: ["SubAdd1a-h1"], title: "Substitution", text: "After substituting $$x=\\frac{3}{2}$$ into the equation, we get $$\\left(4\\right) \\frac{3}{2}-\\left(2\\right)=\\left(2\\right) \\frac{3}{2}+\\left(1\\right)$$"}, {id: "SubAdd1a-h3", type: "hint", dependencies: ["SubAdd1a-h2"], title: "Simplification", text: "Simplify the expressions on both sides of the equation."}, {id: "SubAdd1a-h4", type: "scaffold", problemType: "TextBox", answerType: "arithmetic", hintAnswer: ["6/2"], dependencies: ["SubAdd1a-h3"], title: "Simplification", text: "Simplify the left side of the equation."}, {id: "SubAdd1a-h5", type: "scaffold", problemType: "TextBox", answerType: "arithmetic", hintAnswer: ["3+1"], dependencies: ["SubAdd1a-h4"], title: "Simplification", text: "Simplify the right side of the equation."}, {id: "SubAdd1a-h6", type: "hint", dependencies: ["SubAdd1a-h5"], title: "Comparison", text: "Determine whether the resulting equation is true."}, {id: "SubAdd1a-h7", type: "scaffold", problemType: "MultipleChoice", answerType: "string", hintAnswer: ["True"], dependencies: ["SubAdd1a-h6"], title: "Comparison", text: "Determine whether 6-2 equals $$\\left(3\\right)+\\left(1\\right)$$", choices: ["TRUE", "FALSE"]}, ]; export {hints};