---
declaration: section
origin: cited
lean: MathlibExt.Analysis.ContinuumLimsupConstantWanted.Entire, MathlibExt.Analysis.ContinuumLimsupConstantWanted.RecedesToInf, MathlibExt.Analysis.ContinuumLimsupConstantWanted.Ratio, MathlibExt.Analysis.ContinuumLimsupConstantWanted.conjecture, MathlibExt.Analysis.ContinuumLimsupConstantWanted.conjecture_holds
statement: formalized
---

# Growth of entire functions along continua

5 results, 4 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/entire-functions/growth-of-entire-functions-along-continua/index.html).

## Entire functions

A function $f : \mathbb{C} \to \mathbb{C}$ is entire when it is complex
differentiable at every point of $\mathbb{C}$.

## Sources

- the problem record gives $f$ entire only as ambient context from Hayman; it is taken here as an explicit hypothesis.

Formalized by `MathlibExt.Analysis.ContinuumLimsupConstantWanted.Entire`, a definition declared in [WantedExt/Analysis/ContinuumLimsupConstantWanted.lean, line 35](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/ContinuumLimsupConstantWanted.lean#L35). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/entire-functions/growth-of-entire-functions-along-continua/index.html#entire).

## Continua receding to infinity

A set $\Gamma \subseteq \mathbb{C}$ is a continuum receding
to infinity when it is closed, connected and unbounded.

Here a continuum is read as a closed connected set and receding to infinity as unbounded;
compactness is not required, since an unbounded set is never compact.

Formalized by `MathlibExt.Analysis.ContinuumLimsupConstantWanted.RecedesToInf`, a definition declared in [WantedExt/Analysis/ContinuumLimsupConstantWanted.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/ContinuumLimsupConstantWanted.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/entire-functions/growth-of-entire-functions-along-continua/index.html#recedes-to-inf).

## Ratio of $\log |f|$ to the logarithm of the maximum modulus

For a function
$f : \mathbb{C} \to \mathbb{C}$ and a point $z \in \mathbb{C}$, this is the extended real number
equal to $-\infty$ if $f(z) = 0$, and otherwise to the real number
$\log |f(z)| / \log M(f, |z|)$, where $M(f, r)$ is the Wiman maximum modulus of $f$, $\log 0$ is
taken to be $0$, and division by $0$ gives $0$.

Formalized by `MathlibExt.Analysis.ContinuumLimsupConstantWanted.Ratio`, a definition declared in [WantedExt/Analysis/ContinuumLimsupConstantWanted.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/ContinuumLimsupConstantWanted.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/entire-functions/growth-of-entire-functions-along-continua/index.html#ratio).

## Lower bound $-1$ for the log-modulus ratio along continua

Write $M(f, r)$ for the Wiman
maximum modulus of a function $f : \mathbb{C} \to \mathbb{C}$ at radius $r$. This is the statement
that for every entire, transcendental function $f$ and every continuum $\Gamma$ receding to
infinity (a closed, connected, unbounded subset of $\mathbb{C}$), the limit superior, as
$|z| \to \infty$ with $z \in \Gamma$, of the extended real ratio $\log |f(z)| / \log M(f, |z|)$
is at least $-1$. Here the ratio is taken to be $-\infty$ where $f(z) = 0$, and $0$ where
$f(z) \ne 0$ and $\log M(f, |z|) = 0$.

Transcendence is the standing hypothesis of Hayman's problem; without it the zero function would
be a counterexample, its ratio being constantly $-\infty$.

## Sources

- problem record AMR-022-2035.

Formalized by `MathlibExt.Analysis.ContinuumLimsupConstantWanted.conjecture`, a definition declared in [WantedExt/Analysis/ContinuumLimsupConstantWanted.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/ContinuumLimsupConstantWanted.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/entire-functions/growth-of-entire-functions-along-continua/index.html#conjecture).

## Hayman–Kjellberg theorem on continua receding to infinity

Write $M(f, r)$ for the Wiman
maximum modulus of a function $f : \mathbb{C} \to \mathbb{C}$ at radius $r$. For every entire,
transcendental function $f$ and every closed, connected, unbounded set
$\Gamma \subseteq \mathbb{C}$, the limit superior, as $|z| \to \infty$ with $z \in \Gamma$, of the
extended real ratio $\log |f(z)| / \log M(f, |z|)$ is at least $-1$. Here the ratio is taken to
be $-\infty$ where $f(z) = 0$, and $0$ where $f(z) \ne 0$ and $\log M(f, |z|) = 0$.

Hayman and Kjellberg (Studies in Pure Mathematics, Birkhauser 1983) proved that for entire $f$ and
every $K > 1$ all components of $\{z : \log |f(z)| + K \log M(f, |z|) < 0\}$ are bounded, so the
absolute constant in Hayman–Lingham Problem 2.35 is $A = 1$.

## Sources

- A. Eremenko and J. K. Langley, Meromorphic functions of one complex variable. A survey, arXiv:0801.0692 (2008), https://arxiv.org/abs/0801.0692; Walter K. Hayman and Eleanor F. Lingham, Research Problems in Function Theory (New Edition), arXiv:1809.07200v2 (2018), https://arxiv.org/abs/1809.07200.

Stated but not proved: `MathlibExt.Analysis.ContinuumLimsupConstantWanted.conjecture_holds` is written with `theorem_wanted` in [WantedExt/Analysis/ContinuumLimsupConstantWanted.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/ContinuumLimsupConstantWanted.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/entire-functions/growth-of-entire-functions-along-continua/index.html#conjecture-holds).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Growth of entire functions along continua](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/entire-functions/growth-of-entire-functions-along-continua/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Analysis/complex-analysis/entire-functions/growth-of-entire-functions-along-continua)
