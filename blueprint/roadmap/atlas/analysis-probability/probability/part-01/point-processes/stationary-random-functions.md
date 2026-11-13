---
declaration: section
origin: cited
lean: MathlibExt.Probability.ScottishBook180Wanted.IsStationary, MathlibExt.Probability.ScottishBook180Wanted.ScottishBookProblem180Claim, MathlibExt.Probability.ScottishBook180Wanted.scottishBook180_refuted
statement: formalized
---

# Stationary random functions

3 results, 2 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/point-processes/stationary-random-functions/index.html).

## Stationary random functions (Slutsky–Khinchin)

Let $\mu$ be a measure on a measurable
space $\Omega$, and let $v$ assign to each real $t$ a function $v_t : \Omega \to \mathbb{R}$.
Then $v$ is stationary if there are a real number $c$ and a function $R : \mathbb{R} \to \mathbb{R}$
such that for all real $t$ and $h$, $\int v_t \, d\mu = 0$, $\int v_t^2 \, d\mu = c$ and
$\int v_t \, v_{t+h} \, d\mu = R(h)$.

The integrals are Bochner integrals, which are $0$ for non-integrable functions, so integrability
of $v_t$, $v_t^2$ and $v_t v_{t+h}$ is not required.

Formalized by `MathlibExt.Probability.ScottishBook180Wanted.IsStationary`, a definition declared in [WantedExt/Probability/ScottishBook180Wanted.lean, line 26](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Probability/ScottishBook180Wanted.lean#L26). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/point-processes/stationary-random-functions/index.html#is-stationary).

## Scottish Book Problem 180 (Kampé de Fériet's claim)

The claim that for every probability
space $(\Omega, \mu)$ that carries a measurable random variable $U : \Omega \to \mathbb{R}$
uniformly distributed on $[0, 1]$, and every stationary random function $v$ on $\Omega$ (in the
sense of Slutsky and Khinchin) such that each $v_t : \Omega \to \mathbb{R}$ is measurable, there
exist a measurable random variable $A : \Omega \to \mathbb{R}$ uniformly distributed on $[0, 1]$
and a map $\varphi : \mathbb{R} \to \Omega$ such that $A(\varphi(\alpha)) = \alpha$ for every
$\alpha \in [0, 1]$, and such that for all real $t_1 \ne t_2$ the functions
$\alpha \mapsto v_{t_1}(\varphi(\alpha))$ and $\alpha \mapsto v_{t_2}(\varphi(\alpha))$ are
independent with respect to Lebesgue measure on $[0, 1]$.

Here a variable is uniformly distributed on $[0, 1]$ when its law is Lebesgue measure restricted
to $[0, 1]$. The equation $A(\varphi(\alpha)) = \alpha$ is condition (1) of the problem and the
independence, in the sense of Steinhaus, is condition (2). The existence of $U$ is an added
hypothesis; it rules out refutations that only exploit a space carrying no uniform variable.

Formalized by `MathlibExt.Probability.ScottishBook180Wanted.ScottishBookProblem180Claim`, a definition declared in [WantedExt/Probability/ScottishBook180Wanted.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Probability/ScottishBook180Wanted.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/point-processes/stationary-random-functions/index.html#scottish-book-problem180-claim).

## Scottish Book Problem 180 fails

The claim of Scottish Book Problem 180 is false: there are a
probability space $(\Omega, \mu)$ carrying a measurable random variable uniformly distributed on
$[0, 1]$ and a stationary random function $v$ on $\Omega$ with every $v_t$ measurable, such that
no measurable random variable $A : \Omega \to \mathbb{R}$ uniformly distributed on $[0, 1]$ and no
map $\varphi : \mathbb{R} \to \Omega$ satisfy both $A(\varphi(\alpha)) = \alpha$ for every
$\alpha \in [0, 1]$ and, for all real $t_1 \ne t_2$, the independence of
$\alpha \mapsto v_{t_1}(\varphi(\alpha))$ and $\alpha \mapsto v_{t_2}(\varphi(\alpha))$ with
respect to Lebesgue measure on $[0, 1]$.

A counterexample is $\Omega = \mathbb{R}$ with $\mu$ Lebesgue measure restricted to $[0, 1]$, the
identity as uniform variable, and $v_t(\omega) = \omega - 1/2$ for every $t$, which is stationary
with $c = R(h) = 1/12$. If $A$ and $\varphi$ existed, $\varphi$ would be injective on $[0, 1]$,
while both functions in the independence condition equal $f(\alpha) = \varphi(\alpha) - 1/2$. A
function independent of itself is almost everywhere constant, and an injective function on
$[0, 1]$ is not. No non-degeneracy hypothesis is added, since the source asks for none.

## Sources

- J. Kampe de Feriet, Problem 180 of the Scottish Book, typescript PDF pp. 82-83, printed pp. 79-80; see the commentary in R. D. Mauldin (ed.), The Scottish Book, 2nd ed. (Birkhäuser, 2015).

Stated but not proved: `MathlibExt.Probability.ScottishBook180Wanted.scottishBook180_refuted` is written with `theorem_wanted` in [WantedExt/Probability/ScottishBook180Wanted.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Probability/ScottishBook180Wanted.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/point-processes/stationary-random-functions/index.html#scottish-book180-refuted).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Stationary random functions](https://deicyde.github.io/atlas-lean/roadmap/Probability/point-processes/stationary-random-functions/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Probability/point-processes/stationary-random-functions)
