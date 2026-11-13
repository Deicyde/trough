---
declaration: section
origin: cited
lean: MathlibExt.NumberTheory.SchurSiegelSmyth.conjugates, MathlibExt.NumberTheory.SchurSiegelSmyth.degree, MathlibExt.NumberTheory.SchurSiegelSmyth.trace, MathlibExt.NumberTheory.SchurSiegelSmyth.absoluteTrace, MathlibExt.NumberTheory.SchurSiegelSmyth.IsTotallyPositive, MathlibExt.NumberTheory.SchurSiegelSmyth.trace_pos_re, MathlibExt.NumberTheory.SchurSiegelSmyth.trace_im_eq_zero, MathlibExt.NumberTheory.SchurSiegelSmyth.absoluteTrace_pos
statement: formalized
---

# Schur–Siegel–Smyth trace problem

26 results, 18 proved and 8 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/heights-mahler-measure/schur-siegel-smyth-trace-problem/index.html).

## Conjugates

The conjugates of a complex number $\alpha$ are the roots in $\mathbb{C}$ of
its minimal polynomial over $\mathbb{Q}$, counted with multiplicity. If $\alpha$ is
transcendental, its minimal polynomial is taken to be $0$ and it has no conjugates.

Formalized by `MathlibExt.NumberTheory.SchurSiegelSmyth.conjugates`, a definition declared in [MathlibExt/NumberTheory/Height/SchurSiegelSmyth.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Height/SchurSiegelSmyth.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/heights-mahler-measure/schur-siegel-smyth-trace-problem/index.html#conjugates).

## Degree of a complex number

The degree of a complex number $\alpha$ is the degree of its
minimal polynomial over $\mathbb{Q}$. If $\alpha$ is transcendental, its minimal polynomial is
taken to be $0$, so its degree is $0$.

Formalized by `MathlibExt.NumberTheory.SchurSiegelSmyth.degree`, a definition declared in [MathlibExt/NumberTheory/Height/SchurSiegelSmyth.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Height/SchurSiegelSmyth.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/heights-mahler-measure/schur-siegel-smyth-trace-problem/index.html#degree).

## Trace as the sum of conjugates

For $\alpha \in \mathbb{C}$, the trace of $\alpha$ is
the sum of its conjugates, that is, of the roots in $\mathbb{C}$ of the minimal polynomial of
$\alpha$ over $\mathbb{Q}$, counted with multiplicity. For transcendental $\alpha$ there are no
conjugates and the trace is $0$.

Formalized by `MathlibExt.NumberTheory.SchurSiegelSmyth.trace`, a definition declared in [MathlibExt/NumberTheory/Height/SchurSiegelSmyth.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Height/SchurSiegelSmyth.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/heights-mahler-measure/schur-siegel-smyth-trace-problem/index.html#trace).

## Absolute trace

The absolute trace of a complex number $\alpha$ is the real number
obtained by dividing the real part of the trace of $\alpha$ by the degree of $\alpha$. If
$\alpha$ is transcendental, its trace and its degree are both $0$, and its absolute trace is
taken to be $0$.

For algebraic $\alpha$ the trace is real, and for a totally positive algebraic integer $\alpha$
the absolute trace is the mean of the conjugates of $\alpha$.

Formalized by `MathlibExt.NumberTheory.SchurSiegelSmyth.absoluteTrace`, a definition declared in [MathlibExt/NumberTheory/Height/SchurSiegelSmyth.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Height/SchurSiegelSmyth.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/heights-mahler-measure/schur-siegel-smyth-trace-problem/index.html#absolute-trace).

## Totally positive algebraic integers

A complex number $\alpha$ is a totally positive
algebraic integer when it is integral over $\mathbb{Z}$ and every conjugate of $\alpha$ (every
root in $\mathbb{C}$ of its minimal polynomial over $\mathbb{Q}$) is a strictly positive real
number.

Formalized by `MathlibExt.NumberTheory.SchurSiegelSmyth.IsTotallyPositive`, a definition declared in [MathlibExt/NumberTheory/Height/SchurSiegelSmyth.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Height/SchurSiegelSmyth.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/heights-mahler-measure/schur-siegel-smyth-trace-problem/index.html#is-totally-positive).

## The trace of a totally positive algebraic integer has positive real part

If
$\alpha \in \mathbb{C}$ is a totally positive algebraic integer, then the real part of the trace
of $\alpha$ is strictly positive.

Formalized by `MathlibExt.NumberTheory.SchurSiegelSmyth.trace_pos_re`, a theorem declared in [MathlibExt/NumberTheory/Height/SchurSiegelSmyth.lean, line 113](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Height/SchurSiegelSmyth.lean#L113). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/heights-mahler-measure/schur-siegel-smyth-trace-problem/index.html#trace-pos-re).

## The trace of a totally positive algebraic integer is real

If $\alpha \in \mathbb{C}$ is
a totally positive algebraic integer, then the imaginary part of the trace of $\alpha$ is $0$.

Formalized by `MathlibExt.NumberTheory.SchurSiegelSmyth.trace_im_eq_zero`, a theorem declared in [MathlibExt/NumberTheory/Height/SchurSiegelSmyth.lean, line 130](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Height/SchurSiegelSmyth.lean#L130). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/heights-mahler-measure/schur-siegel-smyth-trace-problem/index.html#trace-im-eq-zero).

## Positivity of the absolute trace

If a complex number $\alpha$ is a totally positive
algebraic integer, then the absolute trace of $\alpha$ is strictly positive.

Formalized by `MathlibExt.NumberTheory.SchurSiegelSmyth.absoluteTrace_pos`, a theorem declared in [MathlibExt/NumberTheory/Height/SchurSiegelSmyth.lean, line 145](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Height/SchurSiegelSmyth.lean#L145). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/heights-mahler-measure/schur-siegel-smyth-trace-problem/index.html#absolute-trace-pos).

## Minimal polynomial of one

The minimal polynomial of $1 \in \mathbb{C}$ over $\mathbb{Q}$
is $X - 1$.

Formalized by `MathlibExt.NumberTheory.SchurSiegelSmyth.minpoly_rat_one_eq`, a theorem declared in [MathlibExt/NumberTheory/Height/SchurSiegelSmyth.lean, line 150](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Height/SchurSiegelSmyth.lean#L150). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/heights-mahler-measure/schur-siegel-smyth-trace-problem/index.html#minpoly-rat-one-eq).

## One is a totally positive algebraic integer

The complex number $1$ is a totally
positive algebraic integer.

Formalized by `MathlibExt.NumberTheory.SchurSiegelSmyth.isTotallyPositive_one`, a theorem declared in [MathlibExt/NumberTheory/Height/SchurSiegelSmyth.lean, line 163](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Height/SchurSiegelSmyth.lean#L163). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/heights-mahler-measure/schur-siegel-smyth-trace-problem/index.html#is-totally-positive-one).

## Admissible trace bounds

A real number $\rho$ is admissible when $\rho \ge 0$ and only
finitely many totally positive algebraic integers $\alpha \in \mathbb{C}$ have absolute trace
less than $\rho$.

Formalized by `MathlibExt.NumberTheory.SchurSiegelSmyth.IsAdmissible`, a definition declared in [MathlibExt/NumberTheory/Height/SchurSiegelSmyth.lean, line 178](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Height/SchurSiegelSmyth.lean#L178). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/heights-mahler-measure/schur-siegel-smyth-trace-problem/index.html#is-admissible).

## Schur–Siegel–Smyth trace constant

The Schur–Siegel–Smyth trace constant $C_{86}$ is
the supremum, taken in the extended reals, of the admissible real bounds: the real numbers
$\rho \ge 0$ such that only finitely many complex numbers that are totally positive algebraic
integers have absolute trace less than $\rho$.

The extended-real value is $-\infty$ for an empty admissible set and $+\infty$ for an unbounded
one; finiteness is the content of the known upper bounds.

Formalized by `MathlibExt.NumberTheory.SchurSiegelSmyth.schurSiegelSmythConstant`, a definition declared in [MathlibExt/NumberTheory/Height/SchurSiegelSmyth.lean, line 186](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Height/SchurSiegelSmyth.lean#L186). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/heights-mahler-measure/schur-siegel-smyth-trace-problem/index.html#schur-siegel-smyth-constant).

## Admissible bounds lie below the Schur–Siegel–Smyth constant

Let $C_{86}$ be the
Schur–Siegel–Smyth trace constant, an extended real number. Every admissible real number $\rho$
satisfies $\rho \le C_{86}$ in the extended reals.

Formalized by `MathlibExt.NumberTheory.SchurSiegelSmyth.coe_le_schurSiegelSmythConstant`, a theorem declared in [MathlibExt/NumberTheory/Height/SchurSiegelSmyth.lean, line 205](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Height/SchurSiegelSmyth.lean#L205). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/heights-mahler-measure/schur-siegel-smyth-trace-problem/index.html#coe-le-schur-siegel-smyth-constant).

## Upper bounds for the Schur–Siegel–Smyth constant

For every extended real number $b$, the
Schur–Siegel–Smyth trace constant is at most $b$ if and only if every admissible real number
$c$ satisfies $c \le b$.

Formalized by `MathlibExt.NumberTheory.SchurSiegelSmyth.schurSiegelSmythConstant_le_iff`, a theorem declared in [MathlibExt/NumberTheory/Height/SchurSiegelSmyth.lean, line 211](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Height/SchurSiegelSmyth.lean#L211). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/heights-mahler-measure/schur-siegel-smyth-trace-problem/index.html#schur-siegel-smyth-constant-le-iff).

## Sum of the conjugates of a complex number

For a complex number $\alpha$, the trace
$\operatorname{tr}(\alpha) \in \mathbb{C}$ is the sum, counted with multiplicity, of the complex
roots of the minimal polynomial of $\alpha$ over $\mathbb{Q}$. When $\alpha$ is algebraic these
roots are the conjugates $\alpha_1, \dots, \alpha_n$ of $\alpha$, so
$\operatorname{tr}(\alpha) = \alpha_1 + \dots + \alpha_n$; when $\alpha$ is transcendental its
minimal polynomial is $0$ by convention and $\operatorname{tr}(\alpha) = 0$.

Formalized by `MathlibExt.NumberTheory.AlgebraicIntegersWanted.AlgebraicIntegers.trace`, a definition declared in [WantedExt/NumberTheory/AlgebraicIntegersWanted.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/AlgebraicIntegersWanted.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/heights-mahler-measure/schur-siegel-smyth-trace-problem/index.html#trace-2).

## Degree of a complex number over the rationals

For a complex number $\alpha$, the degree
$\deg(\alpha)$ is the natural number given by the degree of the minimal polynomial of $\alpha$ over
$\mathbb{Q}$. When $\alpha$ is transcendental its minimal polynomial is $0$ by convention, so
$\deg(\alpha) = 0$.

Formalized by `MathlibExt.NumberTheory.AlgebraicIntegersWanted.AlgebraicIntegers.degree`, a definition declared in [WantedExt/NumberTheory/AlgebraicIntegersWanted.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/AlgebraicIntegersWanted.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/heights-mahler-measure/schur-siegel-smyth-trace-problem/index.html#degree-2).

## Totally positive algebraic numbers

A complex number $\alpha$ is totally positive if it is
algebraic over $\mathbb{Q}$ and every complex root of its minimal polynomial over $\mathbb{Q}$,
that is, every conjugate of $\alpha$, is a positive real number.

Formalized by `MathlibExt.NumberTheory.AlgebraicIntegersWanted.AlgebraicIntegers.IsTotallyPositive`, a definition declared in [WantedExt/NumberTheory/AlgebraicIntegersWanted.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/AlgebraicIntegersWanted.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/heights-mahler-measure/schur-siegel-smyth-trace-problem/index.html#is-totally-positive-2).

## The Schur–Siegel–Smyth constant $\lambda_{\mathrm{SSS}}$

Let $\lambda_{\mathrm{SSS}}$ be
the supremum in $\mathbb{R}$ of the set of real numbers $\lambda$ such that, for every
$\varepsilon > 0$, only finitely many complex numbers $\alpha$ are totally positive algebraic
integers with $\operatorname{tr}(\alpha) < (\lambda - \varepsilon) \deg(\alpha)$, where
$\operatorname{tr}(\alpha)$ and $\deg(\alpha)$ are the trace and the degree of $\alpha$ over
$\mathbb{Q}$ (the trace of a totally positive $\alpha$ is real). By the convention for suprema in
$\mathbb{R}$, $\lambda_{\mathrm{SSS}} = 0$ if this set is empty or unbounded above.

The set is closed downwards and contains its supremum when it is nonempty and bounded above, so
$\lambda_{\mathrm{SSS}}$ is then the greatest such $\lambda$. The source says "least real number",
but this is a typo, as the set has no lower bound. The greatest real number agrees with Orloski,
Sardari and Smith, "New lower bounds for the Schur-Siegel-Smyth trace problem"
(arXiv:2401.03252), where $\lambda_{\mathrm{SSS}}$ is the limit inferior of
$\operatorname{tr}(\alpha)/\deg(\alpha)$ over all totally positive algebraic integers $\alpha$.

Formalized by `MathlibExt.NumberTheory.AlgebraicIntegersWanted.AlgebraicIntegers.lambda_SSS`, a definition declared in [WantedExt/NumberTheory/AlgebraicIntegersWanted.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/AlgebraicIntegersWanted.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/heights-mahler-measure/schur-siegel-smyth-trace-problem/index.html#lambda-sss).

## Smith's theorem on the Schur–Siegel–Smyth trace problem

The Schur–Siegel–Smyth constant
satisfies $\lambda_{\mathrm{SSS}} < 1.89831$; this is Theorem 1.1 of the source.

## Sources

- A. Smith, `Algebraic integers with conjugates in a prescribed distribution`, Annals of Math, 200 (1) 2024. Statement taken from https://github.com/ImperialCollegeLondon/AnnalsChallenge. Problem `annals_algebraic_integers` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.NumberTheory.AlgebraicIntegersWanted.AlgebraicIntegers.theorem_1_1` is written with `theorem_wanted` in [WantedExt/NumberTheory/AlgebraicIntegersWanted.lean, line 94](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/AlgebraicIntegersWanted.lean#L94). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/heights-mahler-measure/schur-siegel-smyth-trace-problem/index.html#theorem-1-1).

## Absolute trace of a totally positive algebraic integer is at least one

For every
complex number $\alpha$ that is a totally positive algebraic integer, the absolute trace of
$\alpha$ is at least $1$.

## Sources

- catalogue trivial lower row, by AM--GM: the absolute trace is at least the geometric mean of the conjugates, whose product is a nonzero rational integer.

Stated but not proved: `MathlibExt.NumberTheory.SchurSiegelSmyth.absoluteTrace_one_le_wanted` is written with `theorem_wanted` in [WantedExt/NumberTheory/Height/SchurSiegelSmythWanted.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Height/SchurSiegelSmythWanted.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/heights-mahler-measure/schur-siegel-smyth-trace-problem/index.html#absolute-trace-one-le-wanted).

## Schur's lower bound for the Schur–Siegel–Smyth constant

The Schur–Siegel–Smyth trace
constant $C_{86}$, an extended real number, satisfies $\sqrt{e} \le C_{86}$.

## Sources

- Schur (1918), lower bound `√e ≤ C₈₆`.

Stated but not proved: `MathlibExt.NumberTheory.SchurSiegelSmyth.schur1918LowerBound_wanted` is written with `theorem_wanted` in [WantedExt/NumberTheory/Height/SchurSiegelSmythWanted.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Height/SchurSiegelSmythWanted.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/heights-mahler-measure/schur-siegel-smyth-trace-problem/index.html#schur1918-lower-bound-wanted).

## Smyth's lower bound for the Schur–Siegel–Smyth constant

The Schur–Siegel–Smyth trace
constant $C_{86}$, an extended real number, satisfies $1.7719 \le C_{86}$.

## Sources

- Smyth (1984), auxiliary-function lower bound `1.7719 ≤ C₈₆`.

Stated but not proved: `MathlibExt.NumberTheory.SchurSiegelSmyth.smyth1984LowerBound_wanted` is written with `theorem_wanted` in [WantedExt/NumberTheory/Height/SchurSiegelSmythWanted.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Height/SchurSiegelSmythWanted.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/heights-mahler-measure/schur-siegel-smyth-trace-problem/index.html#smyth1984-lower-bound-wanted).

## Orloski–Sardari–Smith lower bound for the Schur–Siegel–Smyth constant

The
Schur–Siegel–Smyth trace constant $C_{86}$, an extended real number, satisfies
$1.80203 \le C_{86}$.

## Sources

- Orloski--Sardari--Smith (2025), best known lower bound `1.80203 ≤ C₈₆`.

Stated but not proved: `MathlibExt.NumberTheory.SchurSiegelSmyth.orloskiSardariSmith2025LowerBound_wanted` is written with `theorem_wanted` in [WantedExt/NumberTheory/Height/SchurSiegelSmythWanted.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Height/SchurSiegelSmythWanted.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/heights-mahler-measure/schur-siegel-smyth-trace-problem/index.html#orloski-sardari-smith2025-lower-bound-wa).

## Classical upper bound for the Schur–Siegel–Smyth constant

The Schur–Siegel–Smyth trace
constant $C_{86}$, an extended real number, satisfies $C_{86} \le 2$.

## Sources

- classical upper bound `C₈₆ ≤ 2`, from the totally positive algebraic integers `4 cos^2 (π / n)` whose absolute traces tend to `2`.

Stated but not proved: `MathlibExt.NumberTheory.SchurSiegelSmyth.classicalUpperBound_wanted` is written with `theorem_wanted` in [WantedExt/NumberTheory/Height/SchurSiegelSmythWanted.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Height/SchurSiegelSmythWanted.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/heights-mahler-measure/schur-siegel-smyth-trace-problem/index.html#classical-upper-bound-wanted).

## Smith's upper bound for the Schur–Siegel–Smyth trace constant

The
Schur–Siegel–Smyth trace constant $C_{86}$, an extended real number, satisfies
$C_{86} < 1.89831$.

## Sources

- Smith (2024), strict upper bound `C₈₆ < 1.89831` (the form of Smith's theorem recorded in the neighbouring `AlgebraicIntegersWanted` file as `lambda_SSS < 1.89831`), disproving the conjectured value `2`: infinitely many totally positive algebraic integers have absolute trace below `1.89831`.

Stated but not proved: `MathlibExt.NumberTheory.SchurSiegelSmyth.smith2024UpperBound_wanted` is written with `theorem_wanted` in [WantedExt/NumberTheory/Height/SchurSiegelSmythWanted.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Height/SchurSiegelSmythWanted.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/heights-mahler-measure/schur-siegel-smyth-trace-problem/index.html#smith2024-upper-bound-wanted).

## Sardari–Orloski upper bound for the Schur–Siegel–Smyth constant

The Schur–Siegel–Smyth
trace constant $C_{86}$, an extended real number, satisfies $C_{86} \le 1.8216$.

## Sources

- Sardari--Orloski (2024), best known upper bound `C₈₆ ≤ 1.8216` from explicit limiting measures.

Stated but not proved: `MathlibExt.NumberTheory.SchurSiegelSmyth.sardariOrloski2024UpperBound_wanted` is written with `theorem_wanted` in [WantedExt/NumberTheory/Height/SchurSiegelSmythWanted.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Height/SchurSiegelSmythWanted.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/heights-mahler-measure/schur-siegel-smyth-trace-problem/index.html#sardari-orloski2024-upper-bound-wanted).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Schur–Siegel–Smyth trace problem](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/heights-mahler-measure/schur-siegel-smyth-trace-problem/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/heights-mahler-measure/schur-siegel-smyth-trace-problem)
