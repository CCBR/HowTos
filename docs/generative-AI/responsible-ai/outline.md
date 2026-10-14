
## Description

Title: Responsible AI Use, Validation, and Reproducibility in Bioinformatics

Generative AI models are powerful tools that can enhance research, but they also
pose risks that can be detrimental to our work.
This session will focus on responsible use of AI tools for Bioinformatics to
help researchers get the most out of them while avoiding common pitfalls.
We'll cover best practices for AI use in a research setting including
reproducibility, documentation, and validation for responsible integration of AI
into research workflows.

## Outline

Lesson 3: Responsible Use and Validation focusing on bioinformatics

- Ethical Considerations in Using Generative AI
  - start with general responsible use guidelines, then focus on bioinformatics and data science.
    - https://nih.sharepoint.com/sites/NIH-ai/SitePages/Responsible-AI.aspx
- Validating AI-Generated Code and Outputs (Human-in-the-Loop).
  - Creating tests and validation datasets to ensure accuracy and reliability of AI-generated results.
  - Emphasize the importance of human oversight and critical thinking when using AI tools. Foundational understanding of biology, data science, bioinformatics, and the specific research context is essential for effective use of AI tools. BTEP is useful for this.
- Best Practices for Integrating AI into Research Workflows
  - Version control, reproducibility, and documentation.
- Include specific examples relevant to bioinformatics and data science.
  - Actionable takeaways for participants to implement in their own workflows.

## Brainstorm

- goals of this talk
  - practical advice on how to use genAI well, regardless of which models or tools you're using.
- strengths of genAI

- weaknesses of genAI
  - confirmation bias. sycophantic. genAI tells you what you want to hear.
- risks:
  - ai-gen code:
    - bugs in code leading to incorrect results
    - bad quality code that is hard to maintain, wasting your time
  - ai-gen prose (documentation, issue/PR comments):
    - incorrect details
    - overly verbose, wasting readers' time
    - weird phrases/jargon/ai-"isms", making others distrust your work
  - deskilling
- obligations
  - understand when it is appropriate and not appropriate to use AI
  - literacy, formal and informal training
  - disclose what you're doing, how you're using AI
    - if you rely on AI, write it down in your electronic lab notebook (could be a markdown file in your github repo).
  - guard against AI risks: from wasting time, to wrong answers, to research misconduct
- what does meaningful validation look like?
  - human-in-the-loop is always mandatory
  - zero trust. what outputs are expected? verify the output before committing it.
- NIH AI responsible use guidelines
  - go over main guidelines
  - guidelines do not explicitly tell us how to follow them. here are some practical tips!
- evaluating prompt outputs
  - use genAI as a tool to help you learn. if you don't understand the output, seek to understand it!
  - be critical. add to prompt: "provide counter-factuals". (see Anthropic prompting guidelines/tips)
- gh copilot modes: ask, plan, agent. use ask + plan modes most often, switch to agent mode when you're ready for it to edit/write files.
  - ask for simple questions
  - plan for writing out plan documents. then edit the plan document.
  - give plan document to agent mode to execute.

## Practical tips for responsible AI use in bioinformatics

- Goals
  - Relevant guidance regardless of vendor & model
  - Tips that are unlikely to be solved by models incrementally improving

- Have a plan for how/when you will use GenAI, and how/when you will _not_ use GenAI.
  - GenAI performs well at writing code when the requirements are well defined.
  - e.g. many journals do not allow genAI to be used for writing manuscripts.
- Be thoughtful about how much content you are generating with AI.
  - Can you realistically review all of the output thoroughly?
  - Are you shifting more work to your colleagues?
- Use genAI to **write code**. Don't use genAI to analyze data or write outputs directly. Code is the record for reproducibility.
- Follow reproducible practices always, from the beginning of every project, before you even consider using AI.
  - Be organized. One directory per project. Keep data, code, and outputs in separate directories. Data is read only, and outputs can only be written by code.
  - Use version control. Back up your code to GitHub.
- Review, test, and validate all code (human-written and AI-generated)
  - **Review**: Treat genAI like an untrustworthy stranger. Be skeptical. Do not blindly trust it. Review every response and output. Ensure you understand it. Do not use AI-generated code until you do understand it. Learning opportunity.
  - **Automated testing & validation**:
    - unit and integration testing with simulated and real data, automated with continuous integration workflows.
    - lint / style checkers: GitHub code quality & security scanning (GitHub Advanced Security)
- Document your genAI use. Be transparent about how you use it and which tools you used.
