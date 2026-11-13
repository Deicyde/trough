---
declaration: section
origin: cited
lean: MathlibExt.Probability.CramerDecompositionWanted.cramer_decomposition, MathlibExt.Probability.LevyContinuityWanted.levy_continuity_of_charFun
statement: formalized
proof: formalized
---

# Characteristic functions and generating functions: its own results

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/characteristic-functions/index.html).

Characteristic functions, probability generating functions and positive-definite functions (Bochner), Taylor bounds for characteristic functions, lattice support, Lévy's continuity theorem and Cramér's decomposition theorem for the normal law.

## Cramér's decomposition theorem

Let $X$ and $Y$ be measurable real random variables on a
probability space. If $X$ and $Y$ are independent and $X + Y$ has a Gaussian law, then $X$ and
$Y$ each have a Gaussian law. Here a Gaussian law may be degenerate, that is, a point mass.

## Sources

- H. Cramér, "Über eine Eigenschaft der normalen Verteilungsfunktion", Mathematische Zeitschrift 41 (1936), 405–414, DOI 10.1007/BF01180430.

Formalized by `MathlibExt.Probability.CramerDecompositionWanted.cramer_decomposition`, a theorem declared in [MathlibExt/Probability/CramerDecomposition.lean, line 555](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/CramerDecomposition.lean#L555). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/characteristic-functions/index.html#cramer-decomposition).

## Lévy's continuity theorem

Let $d \in \mathbb{N}$, let $(\mu_n)_{n \in \mathbb{N}}$ be a
sequence of probability measures on the Euclidean space $\mathbb{R}^d$, and let
$\varphi : \mathbb{R}^d \to \mathbb{C}$. Suppose that for every $t \in \mathbb{R}^d$ the
characteristic functions $\hat\mu_n$ of the $\mu_n$ satisfy $\hat\mu_n(t) \to \varphi(t)$ as
$n \to \infty$, and that $\varphi$ is continuous at $0$. Then there is a probability measure $\mu$
on $\mathbb{R}^d$ whose characteristic function is $\varphi$, that is, $\varphi(t) = \hat\mu(t)$
for every $t \in \mathbb{R}^d$, and $\mu_n$ converges weakly to $\mu$.

## Sources

- P. Billingsley, Probability and Measure, 3rd ed., Section 26.

Formalized by `MathlibExt.Probability.LevyContinuityWanted.levy_continuity_of_charFun`, a theorem declared in [MathlibExt/Probability/LevyContinuity.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/LevyContinuity.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/characteristic-functions/index.html#levy-continuity-of-char-fun).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Characteristic functions and generating functions](https://deicyde.github.io/atlas-lean/roadmap/Probability/characteristic-functions/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Probability/characteristic-functions)
