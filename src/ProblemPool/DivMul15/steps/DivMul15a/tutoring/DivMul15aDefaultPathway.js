var hints = [{id: "DivMul15a-h1", type: "hint", dependencies: [], title: "Division property of equality", text: "When you divide both sides of an equation by any non-zero number, you still have equality.", variabilization: {}}, {id: "DivMul15a-h2", type: "scaffold", problemType: "TextBox", answerType: "arithmetic", hintAnswer: ["(5/6)/(-8/3)=-(8/3)r/(-8/3)"], dependencies: ["DivMul15a-h1"], title: "Division", text: "Divide $$\\frac{-\\left(8\\right)}{3}$$ from each side.", variabilization: {}}, {id: "DivMul15a-h3", type: "scaffold", problemType: "TextBox", answerType: "arithmetic", hintAnswer: ["-5/16"], dependencies: ["DivMul15a-h2"], title: "Simplification", text: "What do we get for r after simplifying the equation?", variabilization: {}}, {id: "DivMul15a-h4", type: "hint", dependencies: ["DivMul15a-h3"], title: "Verification", text: "Check whether the result is a solution of the equation.", variabilization: {}}, {id: "DivMul15a-h5", type: "scaffold", problemType: "MultipleChoice", answerType: "string", hintAnswer: ["TRUE"], dependencies: ["DivMul15a-h4"], title: "Verification", text: "Check whether $$\\frac{5}{6}$$ equals $$-\\left(\\frac{8}{3}\\right) \\frac{\\left(-5\\right)}{16}$$.", choices: ["TRUE", "FALSE"], variabilization: {}}, ]; export {hints};