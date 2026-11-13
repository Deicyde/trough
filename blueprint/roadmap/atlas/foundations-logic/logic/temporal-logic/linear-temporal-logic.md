---
declaration: section
origin: cited
lean: Cslib.LTL.Formula, Cslib.LTL.Formula.bot, Cslib.LTL.Formula.or, Cslib.LTL.Formula.imp, Cslib.LTL.Formula.iff, Cslib.LTL.Formula.eventually, Cslib.LTL.Formula.always, Cslib.LTL.Formula.release
statement: formalized
proof: formalized
---

# Linear temporal logic

26 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/temporal-logic/linear-temporal-logic/index.html).

## Formulas of linear temporal logic

For a type $A$ of atoms, the formulas of linear
temporal logic (LTL) over $A$ are generated inductively: every atom $a \in A$ is a formula, the
truth constant $\top$ is a formula, and if $\varphi$ and $\psi$ are formulas then so are the
negation $\neg\varphi$, the conjunction $\varphi \wedge \psi$, the next formula
$\mathbf{X}\,\varphi$ and the until formula $\varphi \mathbin{\mathbf{U}} \psi$.

Formalized by `Cslib.LTL.Formula`, an inductive type declared in [CSLibExt/Logics/LTL/Syntax.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/LTL/Syntax.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/temporal-logic/linear-temporal-logic/index.html#formula).

## Falsity in LTL

The LTL formula $\bot$ (falsity) is defined as $\neg\top$, the negation
of the truth constant $\top$.

Formalized by `Cslib.LTL.Formula.bot`, a definition declared in [CSLibExt/Logics/LTL/Syntax.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/LTL/Syntax.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/temporal-logic/linear-temporal-logic/index.html#bot).

## Disjunction in LTL

For LTL formulas $\varphi$ and $\psi$, the disjunction
$\varphi \vee \psi$ is defined as $\neg(\neg\varphi \wedge \neg\psi)$.

Formalized by `Cslib.LTL.Formula.or`, a definition declared in [CSLibExt/Logics/LTL/Syntax.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/LTL/Syntax.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/temporal-logic/linear-temporal-logic/index.html#or).

## Implication in LTL

For LTL formulas $\varphi$ and $\psi$, the implication
$\varphi \to \psi$ is defined as the disjunction $\neg\varphi \vee \psi$.

Formalized by `Cslib.LTL.Formula.imp`, a definition declared in [CSLibExt/Logics/LTL/Syntax.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/LTL/Syntax.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/temporal-logic/linear-temporal-logic/index.html#imp).

## Bi-implication in LTL

For LTL formulas $\varphi$ and $\psi$, the bi-implication
$\varphi \leftrightarrow \psi$ is defined as the conjunction
$(\varphi \to \psi) \wedge (\psi \to \varphi)$ of the two implications.

Formalized by `Cslib.LTL.Formula.iff`, a definition declared in [CSLibExt/Logics/LTL/Syntax.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/LTL/Syntax.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/temporal-logic/linear-temporal-logic/index.html#iff).

## The eventually operator of LTL

For an LTL formula $\varphi$, the formula
$\mathbf{F}\,\varphi$ ("eventually $\varphi$") is defined as the until formula
$\top \mathbin{\mathbf{U}} \varphi$.

On an ω-word, $\mathbf{F}\,\varphi$ holds at a position exactly when $\varphi$ holds at that
position or at some later one.

Formalized by `Cslib.LTL.Formula.eventually`, a definition declared in [CSLibExt/Logics/LTL/Syntax.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/LTL/Syntax.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/temporal-logic/linear-temporal-logic/index.html#eventually).

## The always operator of LTL

For an LTL formula $\varphi$, the formula
$\mathbf{G}\,\varphi$ ("always $\varphi$") is defined as $\neg\,\mathbf{F}\,\neg\varphi$, the
negation of "eventually $\neg\varphi$".

On an ω-word, $\mathbf{G}\,\varphi$ holds at a position exactly when $\varphi$ holds at that
position and at every later one.

Formalized by `Cslib.LTL.Formula.always`, a definition declared in [CSLibExt/Logics/LTL/Syntax.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/LTL/Syntax.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/temporal-logic/linear-temporal-logic/index.html#always).

## The release operator of LTL

For LTL formulas $\varphi$ and $\psi$, the release
formula $\varphi \mathbin{\mathbf{R}} \psi$ is defined as
$\neg(\neg\varphi \mathbin{\mathbf{U}} \neg\psi)$, the dual of until.

On an ω-word, $\varphi \mathbin{\mathbf{R}} \psi$ holds at a position when, from that position on,
$\psi$ holds up to and including the first position where $\varphi$ holds, or forever if there is
no such position.

Formalized by `Cslib.LTL.Formula.release`, a definition declared in [CSLibExt/Logics/LTL/Syntax.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/LTL/Syntax.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/temporal-logic/linear-temporal-logic/index.html#release).

## Satisfaction of LTL formulas on ω-words

Let $v$ be a valuation that says which atoms are
true at each letter, and for an ω-word $w$ and a natural number $k$ let $w^{(k)}$ be the suffix
$i \mapsto w(k + i)$. Whether $w$ satisfies an LTL formula $\varphi$ under $v$, written
$w \models \varphi$, is defined by recursion on $\varphi$: an atom $a$ holds when $v$ makes $a$
true at the first letter $w(0)$; truth always holds; $\neg \varphi$ holds when $\varphi$ does
not; $\varphi \wedge \psi$ holds when both $\varphi$ and $\psi$ do; $\mathsf{X}\, \varphi$ (next
$\varphi$) holds when $w^{(1)} \models \varphi$; and $\varphi \mathbin{\mathsf{U}} \psi$
($\varphi$ until $\psi$) holds when there is a $k$ with $w^{(k)} \models \psi$ and
$w^{(j)} \models \varphi$ for all $j < k$.

Formalized by `Cslib.LTL.Word.Satisfies`, a definition declared in [CSLibExt/Logics/LTL/OmegaWord.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/LTL/OmegaWord.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/temporal-logic/linear-temporal-logic/index.html#satisfies).

## Satisfaction at a position

Let $v$ be a valuation of atoms on letters, $w$ an ω-word, $k$
a natural number and $\varphi$ an LTL formula. Then $\varphi$ holds at position $k$ of $w$ under
$v$ when the suffix of $w$ starting at position $k$, the ω-word $i \mapsto w(k + i)$, satisfies
$\varphi$ under $v$.

Formalized by `Cslib.LTL.Word.SatisfiesAt`, a definition declared in [CSLibExt/Logics/LTL/OmegaWord.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/LTL/OmegaWord.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/temporal-logic/linear-temporal-logic/index.html#satisfies-at).

## Language of an LTL formula

Given a valuation $v$ of atoms on letters, the ω-language of
an LTL formula $\varphi$ is the set of ω-words that satisfy $\varphi$ under $v$.

Formalized by `Cslib.LTL.Word.language`, a definition declared in [CSLibExt/Logics/LTL/OmegaWord.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/LTL/OmegaWord.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/temporal-logic/linear-temporal-logic/index.html#language).

## Satisfaction at position zero

For every valuation of atoms on letters, ω-word $w$ and LTL
formula $\varphi$, $\varphi$ holds at position $0$ of $w$ if and only if $w$ satisfies $\varphi$.

Formalized by `Cslib.LTL.Word.satisfiesAt_zero`, a theorem declared in [CSLibExt/Logics/LTL/OmegaWord.lean, line 91](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/LTL/OmegaWord.lean#L91). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/temporal-logic/linear-temporal-logic/index.html#satisfies-at-zero).

## Satisfaction on a suffix

Let $w$ be an ω-word and, for a natural number $k$, let
$w^{(k)}$ be its suffix starting at position $k$, the ω-word $i \mapsto w(k + i)$. For every
valuation of atoms on letters, every LTL formula $\varphi$ and every natural number $j$,
$\varphi$ holds at position $j$ of $w^{(k)}$ if and only if $\varphi$ holds at position $k + j$
of $w$.

Formalized by `Cslib.LTL.Word.satisfiesAt_drop`, a theorem declared in [CSLibExt/Logics/LTL/OmegaWord.lean, line 96](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/LTL/OmegaWord.lean#L96). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/temporal-logic/linear-temporal-logic/index.html#satisfies-at-drop).

## Satisfaction of an atom

For every valuation $v$ of atoms on letters, every ω-word $w$
and every atom $a$, the word $w$ satisfies the atomic formula $a$ under $v$ if and only if $v$
makes $a$ true at the first letter $w_0$ of $w$.

Formalized by `Cslib.LTL.Word.Satisfies.atom_iff`, a theorem declared in [CSLibExt/Logics/LTL/OmegaWord.lean, line 111](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/LTL/OmegaWord.lean#L111). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/temporal-logic/linear-temporal-logic/index.html#atom-iff).

## Falsity is never satisfied

For every valuation $v$ of atoms on letters and every
ω-word $w$, the word $w$ does not satisfy the LTL formula $\bot$ (falsity) under $v$.

Formalized by `Cslib.LTL.Word.Satisfies.bot_iff`, a theorem declared in [CSLibExt/Logics/LTL/OmegaWord.lean, line 134](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/LTL/OmegaWord.lean#L134). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/temporal-logic/linear-temporal-logic/index.html#bot-iff).

## Semantics of eventually

For every valuation $v$ of atoms on letters, every ω-word $w$
and every LTL formula $\varphi$, the word $w$ satisfies $\mathbf{F}\,\varphi$ (eventually
$\varphi$) under $v$ if and only if for some $k \in \mathbb{N}$ the suffix of $w$ starting at
position $k$ satisfies $\varphi$ under $v$.

Formalized by `Cslib.LTL.Word.Satisfies.eventually_iff`, a theorem declared in [CSLibExt/Logics/LTL/OmegaWord.lean, line 156](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/LTL/OmegaWord.lean#L156). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/temporal-logic/linear-temporal-logic/index.html#eventually-iff).

## Semantics of release

For a valuation of atoms on letters, an ω-word $w$ and LTL formulas
$\varphi$ and $\psi$, $w$ satisfies $\varphi \mathbin{\mathsf{R}} \psi$ ($\varphi$ releases $\psi$)
if and only if for every position $k$, either $\psi$ holds at position $k$ of $w$ or $\varphi$
holds at some position $j < k$ of $w$.

Formalized by `Cslib.LTL.Word.Satisfies.release_iff`, a theorem declared in [CSLibExt/Logics/LTL/OmegaWord.lean, line 166](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/LTL/OmegaWord.lean#L166). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/temporal-logic/linear-temporal-logic/index.html#release-iff).

## Next is self-dual

For every valuation $v$ of atoms on letters, every ω-word $w$ and every
LTL formula $\varphi$, the word $w$ satisfies $\neg\mathbf{X}\,\varphi$ under $v$ if and only if
it satisfies $\mathbf{X}\,\neg\varphi$ under $v$, where $\mathbf{X}$ is the next operator.

Formalized by `Cslib.LTL.Word.Satisfies.not_next`, a theorem declared in [CSLibExt/Logics/LTL/OmegaWord.lean, line 177](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/LTL/OmegaWord.lean#L177). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/temporal-logic/linear-temporal-logic/index.html#not-next).

## Expansion law for until

For every valuation of atoms on letters, ω-word $w$ and LTL
formulas $\varphi$ and $\psi$, $w$ satisfies $\varphi \mathbin{\mathsf{U}} \psi$ ($\varphi$ until
$\psi$) if and only if either $w$ satisfies $\psi$, or $w$ satisfies $\varphi$ and also satisfies
$\mathsf{X}(\varphi \mathbin{\mathsf{U}} \psi)$, that is, next ($\varphi$ until $\psi$).

Formalized by `Cslib.LTL.Word.Satisfies.until_expansion`, a theorem declared in [CSLibExt/Logics/LTL/OmegaWord.lean, line 207](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/LTL/OmegaWord.lean#L207). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/temporal-logic/linear-temporal-logic/index.html#until-expansion).

## Expansion law for release

For every valuation $v$ of atoms on letters, every ω-word $w$
and all LTL formulas $\varphi$ and $\psi$, the word $w$ satisfies
$\varphi \mathbin{\mathcal{R}} \psi$ ($\varphi$ releases $\psi$) under $v$ if and only if it
satisfies $\psi$ and it satisfies $\varphi$ or $\mathbf{X}(\varphi \mathbin{\mathcal{R}} \psi)$,
all under $v$, where $\mathbf{X}$ is the next operator.

Formalized by `Cslib.LTL.Word.Satisfies.release_expansion`, a theorem declared in [CSLibExt/Logics/LTL/OmegaWord.lean, line 233](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/LTL/OmegaWord.lean#L233). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/temporal-logic/linear-temporal-logic/index.html#release-expansion).

## Idempotence of always

For every valuation $v$ of atoms on letters, every ω-word $w$ and
every LTL formula $\varphi$, the word $w$ satisfies $\mathbf{G}\,\mathbf{G}\,\varphi$ under $v$
if and only if it satisfies $\mathbf{G}\,\varphi$ under $v$, where $\mathbf{G}$ is the always
operator.

Formalized by `Cslib.LTL.Word.Satisfies.always_always`, a theorem declared in [CSLibExt/Logics/LTL/OmegaWord.lean, line 256](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/LTL/OmegaWord.lean#L256). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/temporal-logic/linear-temporal-logic/index.html#always-always).

## Always eventually means infinitely often

For every valuation $v$ of atoms on letters,
every ω-word $w$ and every LTL formula $\varphi$, the word $w$ satisfies
$\mathbf{G}\,\mathbf{F}\,\varphi$ (always eventually $\varphi$) under $v$ if and only if there are
infinitely many $k \in \mathbb{N}$ such that the suffix of $w$ starting at position $k$ satisfies
$\varphi$ under $v$.

Formalized by `Cslib.LTL.Word.Satisfies.always_eventually_iff`, a theorem declared in [CSLibExt/Logics/LTL/OmegaWord.lean, line 269](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/LTL/OmegaWord.lean#L269). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/temporal-logic/linear-temporal-logic/index.html#always-eventually-iff).

## Eventually always means from some point on

For every valuation $v$ of atoms on letters,
every ω-word $w$ and every LTL formula $\varphi$, the word $w$ satisfies
$\mathbf{F}\,\mathbf{G}\,\varphi$ (eventually always $\varphi$) under $v$ if and only if there is
$n \in \mathbb{N}$ such that for every $k \ge n$ the suffix of $w$ starting at position $k$
satisfies $\varphi$ under $v$.

Formalized by `Cslib.LTL.Word.Satisfies.eventually_always_iff`, a theorem declared in [CSLibExt/Logics/LTL/OmegaWord.lean, line 280](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/LTL/OmegaWord.lean#L280). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/temporal-logic/linear-temporal-logic/index.html#eventually-always-iff).

## Satisfaction of an atom at a position

Let $v$ be a valuation of atoms on letters, $w$ an
ω-word, $a$ an atom and $k$ a natural number. The atomic formula $a$ holds at position $k$ of $w$
under $v$ if and only if $v$ makes $a$ true at the letter $w(k)$.

Formalized by `Cslib.LTL.Word.satisfiesAt_atom`, a theorem declared in [CSLibExt/Logics/LTL/OmegaWord.lean, line 294](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/LTL/OmegaWord.lean#L294). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/temporal-logic/linear-temporal-logic/index.html#satisfies-at-atom).

## Relabelling the letters of an ω-word

Let $v$ be a valuation of atoms on letters of an
alphabet $\Sigma$, let $f \colon \Sigma' \to \Sigma$ be a map, and let $w$ be an ω-word over
$\Sigma'$. For every LTL formula $\varphi$, the relabelled word $i \mapsto f(w(i))$ satisfies
$\varphi$ under $v$ if and only if $w$ satisfies $\varphi$ under the valuation that makes an atom
$a$ true at a letter $s$ of $\Sigma'$ exactly when $v$ makes $a$ true at $f(s)$.

Formalized by `Cslib.LTL.Word.satisfies_map`, a theorem declared in [CSLibExt/Logics/LTL/OmegaWord.lean, line 315](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/LTL/OmegaWord.lean#L315). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/temporal-logic/linear-temporal-logic/index.html#satisfies-map).

## Membership in the language of a formula

For every valuation $v$ of atoms on letters,
every ω-word $w$ and every LTL formula $\varphi$, the word $w$ belongs to the ω-language of
$\varphi$ under $v$ if and only if $w$ satisfies $\varphi$ under $v$.

Formalized by `Cslib.LTL.Word.mem_language`, a theorem declared in [CSLibExt/Logics/LTL/OmegaWord.lean, line 335](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/LTL/OmegaWord.lean#L335). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/temporal-logic/linear-temporal-logic/index.html#mem-language).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Linear temporal logic](https://deicyde.github.io/atlas-lean/roadmap/Logic/temporal-logic/linear-temporal-logic/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Logic/temporal-logic/linear-temporal-logic)
