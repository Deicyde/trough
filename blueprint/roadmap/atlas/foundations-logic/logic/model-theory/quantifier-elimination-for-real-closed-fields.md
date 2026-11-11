---
declaration: section
origin: cited
lean: MathlibExt.TheoryOfComputation.RealClosedFieldQEWanted.ProgramVerification.RealClosedFieldQE.Term, MathlibExt.TheoryOfComputation.RealClosedFieldQEWanted.ProgramVerification.RealClosedFieldQE.Formula, MathlibExt.TheoryOfComputation.RealClosedFieldQEWanted.ProgramVerification.RealClosedFieldQE.Formula.not, MathlibExt.TheoryOfComputation.RealClosedFieldQEWanted.ProgramVerification.RealClosedFieldQE.Formula.tru, MathlibExt.TheoryOfComputation.RealClosedFieldQEWanted.ProgramVerification.RealClosedFieldQE.Formula.or, MathlibExt.TheoryOfComputation.RealClosedFieldQEWanted.ProgramVerification.RealClosedFieldQE.Formula.and, MathlibExt.TheoryOfComputation.RealClosedFieldQEWanted.ProgramVerification.RealClosedFieldQE.Formula.ex, MathlibExt.TheoryOfComputation.RealClosedFieldQEWanted.ProgramVerification.RealClosedFieldQE.cons
statement: formalized
---

# Quantifier elimination for real closed fields

15 results, 11 proved and 4 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/model-theory/quantifier-elimination-for-real-closed-fields/index.html).

## Syntax

## Terms of the language of ordered rings

Terms are built from variables $x_i$, one for
each natural number $i$ (a de Bruijn index), and integer constants $k \in \mathbb{Z}$, using
addition $s + t$, multiplication $s \cdot t$ and negation $-t$.

Formalized by `MathlibExt.TheoryOfComputation.RealClosedFieldQEWanted.ProgramVerification.RealClosedFieldQE.Term`, an inductive type declared in [WantedExt/TheoryOfComputation/RealClosedFieldQEWanted.lean, line 111](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/TheoryOfComputation/RealClosedFieldQEWanted.lean#L111). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/model-theory/quantifier-elimination-for-real-closed-fields/index.html#term).

## Formulas of the language of ordered rings

Formulas are built from the atomic formulas
$s < t$ and $s = t$, for terms $s$ and $t$, and falsity $\bot$, by implication $\varphi \to \psi$
and universal quantification $\forall \varphi$, which binds de Bruijn index $0$ in $\varphi$.
Negation, truth, disjunction, conjunction and existential quantification are defined from these.

Formalized by `MathlibExt.TheoryOfComputation.RealClosedFieldQEWanted.ProgramVerification.RealClosedFieldQE.Formula`, an inductive type declared in [WantedExt/TheoryOfComputation/RealClosedFieldQEWanted.lean, line 123](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/TheoryOfComputation/RealClosedFieldQEWanted.lean#L123). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/model-theory/quantifier-elimination-for-real-closed-fields/index.html#formula).

## Negation of a formula

The negation $\neg\varphi$ of a formula $\varphi$ is the formula
$\varphi \to \bot$.

Formalized by `MathlibExt.TheoryOfComputation.RealClosedFieldQEWanted.ProgramVerification.RealClosedFieldQE.Formula.not`, a definition declared in [WantedExt/TheoryOfComputation/RealClosedFieldQEWanted.lean, line 136](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/TheoryOfComputation/RealClosedFieldQEWanted.lean#L136). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/model-theory/quantifier-elimination-for-real-closed-fields/index.html#not).

## The true formula

The formula $\top$ is the negation $\neg\bot$ of falsity, that is, the
formula $\bot \to \bot$.

Formalized by `MathlibExt.TheoryOfComputation.RealClosedFieldQEWanted.ProgramVerification.RealClosedFieldQE.Formula.tru`, a definition declared in [WantedExt/TheoryOfComputation/RealClosedFieldQEWanted.lean, line 139](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/TheoryOfComputation/RealClosedFieldQEWanted.lean#L139). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/model-theory/quantifier-elimination-for-real-closed-fields/index.html#tru).

## Disjunction of formulas

The disjunction $\varphi \lor \psi$ of formulas $\varphi$ and
$\psi$ is the formula $\neg\varphi \to \psi$.

Formalized by `MathlibExt.TheoryOfComputation.RealClosedFieldQEWanted.ProgramVerification.RealClosedFieldQE.Formula.or`, a definition declared in [WantedExt/TheoryOfComputation/RealClosedFieldQEWanted.lean, line 142](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/TheoryOfComputation/RealClosedFieldQEWanted.lean#L142). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/model-theory/quantifier-elimination-for-real-closed-fields/index.html#or).

## Conjunction of formulas

For formulas $\varphi$ and $\psi$, the conjunction
$\varphi \wedge \psi$ is the formula $\neg(\varphi \to \neg\psi)$.

Formalized by `MathlibExt.TheoryOfComputation.RealClosedFieldQEWanted.ProgramVerification.RealClosedFieldQE.Formula.and`, a definition declared in [WantedExt/TheoryOfComputation/RealClosedFieldQEWanted.lean, line 145](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/TheoryOfComputation/RealClosedFieldQEWanted.lean#L145). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/model-theory/quantifier-elimination-for-real-closed-fields/index.html#and).

## Existential quantification of formulas

For a formula $\varphi$, the formula
$\exists \varphi$ is $\neg \forall \neg \varphi$; it binds de Bruijn index $0$ in $\varphi$.

Formalized by `MathlibExt.TheoryOfComputation.RealClosedFieldQEWanted.ProgramVerification.RealClosedFieldQE.Formula.ex`, a definition declared in [WantedExt/TheoryOfComputation/RealClosedFieldQEWanted.lean, line 148](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/TheoryOfComputation/RealClosedFieldQEWanted.lean#L148). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/model-theory/quantifier-elimination-for-real-closed-fields/index.html#ex).

## Extending an environment

An environment is a map $e : \mathbb{N} \to \mathbb{R}$ that
assigns a real number to each de Bruijn index. For $x \in \mathbb{R}$, the extension of $e$ by $x$
sends index $0$ to $x$ and index $i + 1$ to $e(i)$ for every $i \in \mathbb{N}$.

Formalized by `MathlibExt.TheoryOfComputation.RealClosedFieldQEWanted.ProgramVerification.RealClosedFieldQE.cons`, a definition declared in [WantedExt/TheoryOfComputation/RealClosedFieldQEWanted.lean, line 160](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/TheoryOfComputation/RealClosedFieldQEWanted.lean#L160). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/model-theory/quantifier-elimination-for-real-closed-fields/index.html#cons).

## Evaluation of terms

Given an environment $e : \mathbb{N} \to \mathbb{R}$, the value of a
term in $\mathbb{R}$ is defined by recursion on the term: the variable with de Bruijn index $i$ has
value $e(i)$, the integer constant $k$ has value $k$, and the value of a sum, product or negation
of terms is the sum, product or negation in $\mathbb{R}$ of the values of its parts.

Formalized by `MathlibExt.TheoryOfComputation.RealClosedFieldQEWanted.ProgramVerification.RealClosedFieldQE.Term.eval`, a definition declared in [WantedExt/TheoryOfComputation/RealClosedFieldQEWanted.lean, line 165](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/TheoryOfComputation/RealClosedFieldQEWanted.lean#L165). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/model-theory/quantifier-elimination-for-real-closed-fields/index.html#eval).

## Satisfaction of formulas over the reals

Let $e : \mathbb{N} \to \mathbb{R}$ be an
environment. Whether a formula holds under $e$ is defined by recursion on the formula: $s < t$
holds when the value of $s$ under $e$ is less than the value of $t$ under $e$; $s = t$ holds when
these values are equal; $\bot$ never holds; $\varphi \to \psi$ holds when $\varphi$ holding under
$e$ implies $\psi$ holding under $e$; and $\forall \varphi$ holds when, for every
$x \in \mathbb{R}$, $\varphi$ holds under the extension of $e$ by $x$.

Formalized by `MathlibExt.TheoryOfComputation.RealClosedFieldQEWanted.ProgramVerification.RealClosedFieldQE.Formula.Holds`, a definition declared in [WantedExt/TheoryOfComputation/RealClosedFieldQEWanted.lean, line 173](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/TheoryOfComputation/RealClosedFieldQEWanted.lean#L173). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/model-theory/quantifier-elimination-for-real-closed-fields/index.html#holds).

## Quantifier-free formulas

A formula is quantifier free if it contains no universal
quantifier $\forall$.

Formalized by `MathlibExt.TheoryOfComputation.RealClosedFieldQEWanted.ProgramVerification.RealClosedFieldQE.Formula.IsQF`, a definition declared in [WantedExt/TheoryOfComputation/RealClosedFieldQEWanted.lean, line 181](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/TheoryOfComputation/RealClosedFieldQEWanted.lean#L181). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/model-theory/quantifier-elimination-for-real-closed-fields/index.html#is-qf).

## Quantifier elimination over the reals

Quantifier elimination is a map sending each formula
$\varphi$ of the language of ordered rings to a formula $\operatorname{qe}(\varphi)$, subject to
two requirements: $\operatorname{qe}(\varphi)$ is quantifier free, and for every environment
$e : \mathbb{N} \to \mathbb{R}$ assigning a real number to each variable,
$\operatorname{qe}(\varphi)$ holds in $\mathbb{R}$ under $e$ if and only if $\varphi$ does.

The formula $\operatorname{qe}(\varphi)$ may mention additional variables, but only vacuously.

## Sources

- Tarski, 'A Decision Method for Elementary Algebra and Geometry' (1951); Collins, 'Quantifier elimination for real closed fields by cylindrical algebraic decomposition' (1975); Mahboubi, 'Programming and certifying a CAD algorithm in the Coq system' (2006); Cohen and Mahboubi, 'Formal proofs in real algebraic geometry: from ordered fields to quantifier elimination' (2012). Problem `rcf_quantifier_elimination` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.TheoryOfComputation.RealClosedFieldQEWanted.ProgramVerification.RealClosedFieldQE.qe` is written with `def_wanted` in [WantedExt/TheoryOfComputation/RealClosedFieldQEWanted.lean, line 195](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/TheoryOfComputation/RealClosedFieldQEWanted.lean#L195). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/model-theory/quantifier-elimination-for-real-closed-fields/index.html#qe).

## Quantifier elimination yields quantifier-free formulas

Let $\mathrm{qe}$ be the quantifier
elimination map on formulas. For every formula $\varphi$, the formula $\mathrm{qe}(\varphi)$ is
quantifier free.

## Sources

- Tarski, 'A Decision Method for Elementary Algebra and Geometry' (1951); Collins, 'Quantifier elimination for real closed fields by cylindrical algebraic decomposition' (1975); Mahboubi, 'Programming and certifying a CAD algorithm in the Coq system' (2006); Cohen and Mahboubi, 'Formal proofs in real algebraic geometry: from ordered fields to quantifier elimination' (2012). Problem `rcf_quantifier_elimination` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.TheoryOfComputation.RealClosedFieldQEWanted.ProgramVerification.RealClosedFieldQE.isQF_qe` is written with `theorem_wanted` in [WantedExt/TheoryOfComputation/RealClosedFieldQEWanted.lean, line 199](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/TheoryOfComputation/RealClosedFieldQEWanted.lean#L199). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/model-theory/quantifier-elimination-for-real-closed-fields/index.html#is-qf-qe).

## Quantifier elimination preserves truth

Let $\mathrm{qe}$ be the quantifier elimination map
on formulas. For every formula $\varphi$ and every environment $e : \mathbb{N} \to \mathbb{R}$,
the formula $\mathrm{qe}(\varphi)$ holds in $\mathbb{R}$ under $e$ if and only if $\varphi$ holds
in $\mathbb{R}$ under $e$.

Together with the statement that $\mathrm{qe}(\varphi)$ is always quantifier free, this is
Tarski's quantifier elimination theorem, stated for $\mathbb{R}$.

## Sources

- Tarski, 'A Decision Method for Elementary Algebra and Geometry' (1951); Collins, 'Quantifier elimination for real closed fields by cylindrical algebraic decomposition' (1975); Mahboubi, 'Programming and certifying a CAD algorithm in the Coq system' (2006); Cohen and Mahboubi, 'Formal proofs in real algebraic geometry: from ordered fields to quantifier elimination' (2012). Problem `rcf_quantifier_elimination` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.TheoryOfComputation.RealClosedFieldQEWanted.ProgramVerification.RealClosedFieldQE.holds_qe` is written with `theorem_wanted` in [WantedExt/TheoryOfComputation/RealClosedFieldQEWanted.lean, line 203](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/TheoryOfComputation/RealClosedFieldQEWanted.lean#L203). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/model-theory/quantifier-elimination-for-real-closed-fields/index.html#holds-qe).

## A real number is a square exactly when it is nonnegative

For every environment
$e : \mathbb{N} \to \mathbb{R}$, the formula $\exists x.\ x \cdot x = a$ holds under $e$ if and
only if the formula $\neg(a < 0)$ holds under $e$. In the first formula the bound variable $x$ is
de Bruijn index $0$ and $a$ is index $1$; in the second $a$ is index $0$; in both, $a$ denotes
$e(0)$. Thus $e(0)$ is a square in $\mathbb{R}$ exactly when $e(0) \ge 0$.

This checks the semantics and the de Bruijn convention against a known fact.

## Sources

- Tarski, 'A Decision Method for Elementary Algebra and Geometry' (1951); Collins, 'Quantifier elimination for real closed fields by cylindrical algebraic decomposition' (1975); Mahboubi, 'Programming and certifying a CAD algorithm in the Coq system' (2006); Cohen and Mahboubi, 'Formal proofs in real algebraic geometry: from ordered fields to quantifier elimination' (2012). Problem `rcf_quantifier_elimination` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.TheoryOfComputation.RealClosedFieldQEWanted.ProgramVerification.RealClosedFieldQE.holds_ex_sq` is written with `theorem_wanted` in [WantedExt/TheoryOfComputation/RealClosedFieldQEWanted.lean, line 211](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/TheoryOfComputation/RealClosedFieldQEWanted.lean#L211). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/model-theory/quantifier-elimination-for-real-closed-fields/index.html#holds-ex-sq).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Quantifier elimination for real closed fields](https://deicyde.github.io/atlas-lean/roadmap/Logic/model-theory/quantifier-elimination-for-real-closed-fields/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Logic/model-theory/quantifier-elimination-for-real-closed-fields)
