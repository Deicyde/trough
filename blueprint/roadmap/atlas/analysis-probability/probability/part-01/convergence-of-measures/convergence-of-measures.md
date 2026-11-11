---
declaration: section
origin: cited
lean: MathlibExt.Probability.CramerWoldWanted.cramer_wold_device, MathlibExt.Probability.ProkhorovSequential.prokhorov_sequential, MathlibExt.Probability.SkorokhodRepresentationWanted.skorokhod_representation
statement: formalized
proof: formalized
---

# Convergence of probability measures: its own results

3 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/convergence-of-measures/index.html).

Weak convergence and convergence in probability, tightness and Prokhorov's theorem, Helly selection, Skorokhod representation, the continuous mapping theorem, the Cramér–Wold device and total variation distance; specific limit laws go to the limit-theorem fields.

## Cramér–Wold device

Let $d$ be a natural number, let $(\Omega, \mu)$ and $(\Omega', \mu')$
be probability spaces, and let $X_n : \Omega \to \mathbb{R}^d$ for $n \in \mathbb{N}$ and
$Z : \Omega' \to \mathbb{R}^d$ be maps, where $\mathbb{R}^d$ carries the Euclidean inner product.
If for every $t \in \mathbb{R}^d$ the real-valued maps $\langle t, X_n \rangle$ converge in
distribution to $\langle t, Z \rangle$ as $n \to \infty$, then $X_n$ converges in distribution
to $Z$ as $n \to \infty$.

Here convergence in distribution means that every $X_n$ and the limit are almost everywhere
measurable and their laws converge weakly as probability measures.

## Sources

- H. Cramér and H. Wold, "Some Theorems on Distribution Functions", Journal of the London Mathematical Society s1-11 (1936), 290–294, DOI 10.1112/jlms/s1-11.4.290.

Formalized by `MathlibExt.Probability.CramerWoldWanted.cramer_wold_device`, a theorem declared in [MathlibExt/Probability/CramerWold.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/CramerWold.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/convergence-of-measures/index.html#cramer-wold-device).

## Prokhorov's theorem, sequential form on $\mathbb{R}$

A sequence $(\mu_n)$ of probability
measures on $\mathbb{R}$ is tight if and only if every subsequence of $(\mu_n)$ has a further
subsequence converging weakly to a probability measure on $\mathbb{R}$.

Formalized by `MathlibExt.Probability.ProkhorovSequential.prokhorov_sequential`, a theorem declared in [MathlibExt/Probability/ProkhorovSequential.lean, line 153](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/ProkhorovSequential.lean#L153). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/convergence-of-measures/index.html#prokhorov-sequential).

## Skorokhod representation theorem

Let $X$ be a Polish space with its Borel
$\sigma$-algebra, let $(\mu_n)_{n \in \mathbb{N}}$ be a sequence of probability measures on $X$,
and let $\mu$ be a probability measure on $X$ such that $\mu_n$ converges weakly to $\mu$. Write
$\lambda$ for Lebesgue measure on $\mathbb{R}$ restricted to $[0, 1]$. Then there exist measurable
maps $Y_n : \mathbb{R} \to X$ for $n \in \mathbb{N}$ and $Y : \mathbb{R} \to X$ such that the
pushforward of $\lambda$ under $Y_n$ is $\mu_n$ for every $n$, the pushforward of $\lambda$ under
$Y$ is $\mu$, and $Y_n(t) \to Y(t)$ as $n \to \infty$ for $\lambda$-almost every $t$.

## Sources

- A. V. Skorokhod, Limit theorems for stochastic processes, Theory Probab. Appl. 1 (1956) 261–290; textbook in Billingsley, Convergence of Probability Measures, 2nd ed., Foundations of Modern Probability (Icc 0 1)` source, `Icc` Lebesgue base; standard version on `[0, 1]` with Lebesgue.

Formalized by `MathlibExt.Probability.SkorokhodRepresentationWanted.skorokhod_representation`, a theorem declared in [MathlibExt/Probability/SkorokhodRepresentation.lean, line 442](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/SkorokhodRepresentation.lean#L442). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/convergence-of-measures/index.html#skorokhod-representation).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Convergence of probability measures](https://deicyde.github.io/atlas-lean/roadmap/Probability/convergence-of-measures/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Probability/convergence-of-measures)
