---
declaration: section
origin: cited
lean: MathlibExt.Probability.DeFinettiWanted.deFinetti_binary, MathlibExt.Probability.KolmogorovExtensionWanted.kolmogorov_extension
statement: formalized
proof: formalized
---

# Foundations of probability: its own results

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/foundations/index.html).

Construction of probability measures and processes (Kolmogorov extension, measures from Stieltjes functions), independence, conditional expectation and regular conditional distributions, exchangeability and de Finetti's theorem, and zero–one laws for sequences (Hewitt–Savage); zero–one laws for continuous processes go to Brownian motion and stochastic calculus, tail sigma-algebras of random walks to Random walks.

## De Finetti's theorem for binary sequences

Let $\mu$ be a probability measure on the space
$\{0, 1\}^{\mathbb{N}}$ of binary sequences $\omega = (\omega_i)_{i \in \mathbb{N}}$, with $0$ and
$1$ standing for false and true. Suppose $\mu$ is exchangeable: for every permutation $\pi$ of
$\mathbb{N}$ that moves only finitely many points, the image of $\mu$ under the map
$\omega \mapsto \omega \circ \pi$ is $\mu$. Then there is a probability measure $\nu$ on $[0, 1]$
such that for all disjoint finite sets $A, B \subseteq \mathbb{N}$,

$$\mu\{\omega : \omega_i = 1 \text{ for all } i \in A \text{ and } \omega_i = 0 \text{ for all }
i \in B\} = \int_{[0, 1]} p^{|A|} (1 - p)^{|B|} \, d\nu(p).$$

## Sources

- B. de Finetti, Funzione caratteristica di un fenomeno aleatorio, Atti Accad. Naz. Lincei 4 (1931) and La prévision: ses lois logiques (1937); textbook in Kallenberg, Probabilistic Symmetries and Invariance Principles; also Durrett, Probability Theory and Examples

Formalized by `MathlibExt.Probability.DeFinettiWanted.deFinetti_binary`, a theorem declared in [MathlibExt/Probability/DeFinetti.lean, line 606](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/DeFinetti.lean#L606). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/foundations/index.html#de-finetti-binary).

## Kolmogorov extension theorem

Let $(\alpha_i)_{i \in \iota}$ be a family of Polish spaces, each
with its Borel σ-algebra, indexed by an arbitrary type $\iota$. For each finite set
$J \subseteq \iota$ let $P_J$ be a probability measure on $\prod_{j \in J} \alpha_j$, and suppose
the family is projective: whenever $J \subseteq I$ are finite, the image of $P_I$ under the
restriction map $\prod_{i \in I} \alpha_i \to \prod_{j \in J} \alpha_j$ is $P_J$. Then there is a
measure $\mu$ on $\prod_{i \in \iota} \alpha_i$ whose image under the restriction map to
$\prod_{j \in J} \alpha_j$ is $P_J$ for every finite $J \subseteq \iota$.

## Sources

- A. N. Kolmogorov, Grundbegriffe der Wahrscheinlichkeitsrechnung, 1933; P. J. Daniell 1918 precursor; textbook in Kallenberg, Foundations of Modern Probability, 3rd ed. (Kolmogorov extension) and Tao, Introduction to Measure Theory Lean Polish Borel projective-limit version; full general version handles standard Borel factors.

Formalized by `MathlibExt.Probability.KolmogorovExtensionWanted.kolmogorov_extension`, a theorem declared in [MathlibExt/Probability/KolmogorovExtension.lean, line 276](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/KolmogorovExtension.lean#L276). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/foundations/index.html#kolmogorov-extension).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Foundations of probability](https://deicyde.github.io/atlas-lean/roadmap/Probability/foundations/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Probability/foundations)
