---
declaration: section
origin: cited
lean: MetaMathlibExt.eulerMaclaurinFormula, MetaMathlibExt.watson_inverse_factorial_series, MetaMathlibExt.watson_laplace_integral_asymptotic
statement: formalized
---

# Asymptotic analysis: its own results

3 results, 2 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/asymptotic-analysis/index.html).

Asymptotic expansions and methods: Euler–Maclaurin and Watson's lemma, Laplace-type integrals, coefficient asymptotics of power series (Bender's lemma), Stirling-type and inverse-factorial expansions, and asymptotic expansions of power sums, Lambert series and log sums; complex-analytic saddle-point results on entire functions go to Complex analysis.

## Euler–Maclaurin formula

Let $a < b$ be integers, let $p \ge 1$ be a natural number, and
let $f : \mathbb{R} \to \mathbb{R}$ be $p$ times continuously differentiable on $[a, b]$, its
derivatives $f^{(k)}$ being taken relative to $[a, b]$ (one-sided at the endpoints). Let $B_j$
be the Bernoulli numbers with $B_1 = -\tfrac{1}{2}$. Then there are $1$-periodic functions
$P_m : \mathbb{R} \to \mathbb{R}$ for $m \ge 0$ such that $P_p$ agrees on $[0, 1)$ with the
Bernoulli polynomial $\sum_{j=0}^{p} \binom{p}{j} B_j x^{p-j}$, and
$\sum_{n=a}^{b} f(n) = I + E + R$, where $I = \int_a^b f(x)\,dx + \frac{f(a) + f(b)}{2}$,
$E = \sum_{k=1}^{\lfloor p/2 \rfloor} \frac{B_{2k}}{(2k)!} (f^{(2k-1)}(b) - f^{(2k-1)}(a))$
and $R = \frac{(-1)^{p+1}}{p!} \int_a^b P_p(x) f^{(p)}(x)\,dx$.

## Sources

- https://en.wikipedia.org/wiki/Euler%E2%80%93Maclaurin_formula.

Formalized by `MetaMathlibExt.eulerMaclaurinFormula`, a theorem declared in [MathlibExt/Analysis/Calculus/EulerMaclaurinFormula.lean, line 809](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Calculus/EulerMaclaurinFormula.lean#L809). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/asymptotic-analysis/index.html#euler-maclaurin-formula).

## Watson's inverse factorial expansion

Let $A,B,\rho,\sigma,\alpha,\delta>0$, $\gamma\ge 0$
and $p$ be real numbers with $\alpha+3\delta\lt \pi/2$ and $1\lt p<1+e^{-\pi\cot\alpha}$. Let $S$ be the
sector $\{z\in\mathbb{C} : |z|>\gamma,\ |\arg z|\le\pi/2+\alpha+3\delta\}$, where $\arg$ is the
principal argument. Let $f$ be a complex function that is analytic at every point of the
half-plane $\{z : \mathrm{Re}\,z>0\}$ and at every point of $S$, let $a_0,a_1,\dots$ be complex
numbers with $|a_n|\lt A\rho^n n!$ for every $n\ge 0$, and let $R_0,R_1,\dots$ be complex functions
such that for every $n\ge 0$ and every $z\in S$

$$f(z)=\sum_{k=0}^{n}\frac{a_k}{z^k}+R_n(z)\qquad\text{and}\qquad|R_n(z)\,z^{n+1}|\lt B\sigma^n n!.$$

Suppose that $M_0$ is the largest real $x>0$ with

$$e^{-2\cos\alpha/(\rho x)}-2\cos\big(\sin\alpha/(\rho x)\big)e^{-\cos\alpha/(\rho x)}+1-p^2=0.$$

Then for every real $M$ with $0\lt M\le M_0$ and every complex $w$ with $\mathrm{Re}\,w\ge 0$ there
are complex numbers $b_0,b_1,\dots$ such that for every $z$ with $\mathrm{Re}\,z>0$ the series

$$\sum_{k=1}^{\infty}\frac{b_k}{(Mz+w+1)(Mz+w+2)\cdots(Mz+w+k)}$$

converges absolutely and its sum is $f(z)-b_0$.

## Sources

- https://cs.uwaterloo.ca/journals/JIS/VOL25/Schumacher/schu9.tex, lines 370-417. Scope exclusion: excludes the `M = 1, w = 0` specialization and the later Stirling-coefficient theorem.

Stated but not proved: `MetaMathlibExt.watson_inverse_factorial_series` is written with `theorem_wanted` in [WantedExt/Analysis/Complex/WatsonInverseFactorial.lean, line 29](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/Complex/WatsonInverseFactorial.lean#L29). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/asymptotic-analysis/index.html#watson-inverse-factorial-series).

## Watson's lemma for Laplace integrals

Let $g : \mathbb{R} \to \mathbb{R}$ and let
$(c_k)_{k \ge 1}$ be real numbers such that for every $N \ge 0$,
$g(s) - \sum_{k=1}^{N} c_k s^k = O(s^{N+1})$ as $s \to 0^+$. Suppose there is $m_0 \in \mathbb{R}$
such that $s \mapsto g(s) e^{-ms}$ is integrable on $(0, \infty)$ for every $m \ge m_0$. Then
for every $N \ge 0$,
$\int_0^\infty g(s) e^{-ms} \, ds - \sum_{k=1}^{N} k! \, c_k / m^{k+1} = O(1 / m^{N+2})$ as
$m \to \infty$.

The case $N = 0$ of the hypothesis says $g(s) = O(s)$ as $s \to 0^+$: the expansion of $g$ has no
constant term.

## Sources

- <https://cs.uwaterloo.ca/journals/JIS/VOL14/Nemes/nemes4.tex>, lines 142-151.

Formalized by `MetaMathlibExt.watson_laplace_integral_asymptotic`, a theorem declared in [MathlibExt/Analysis/Asymptotics/WatsonLaplaceLemma.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Asymptotics/WatsonLaplaceLemma.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/asymptotic-analysis/index.html#watson-laplace-integral-asymptotic).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Asymptotic analysis](https://deicyde.github.io/atlas-lean/roadmap/Analysis/asymptotic-analysis/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/asymptotic-analysis)
