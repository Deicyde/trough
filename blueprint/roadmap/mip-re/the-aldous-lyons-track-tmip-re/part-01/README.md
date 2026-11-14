---
navigation: transparent
---

# Tailored game; II:1243 to $\mathrm{TMIP}^* =…

- [Tailored game; II:1243](def-tailored-game.md)
- [The three forms of a measurement with outcomes in $\mathbb{F}_2^k$; II:972–1006](def-fourier-forms.md)
- [Signed permutations; II:1008–1069](def-signed-perm.md)
- [Z-aligned permutation strategies commuting along edges; II:1043–1057, II:1279–1283](def-zpc-strategy.md)

**Remark (Two conventions).** The paper's loops $xx$ read a single answer, over $S_x$; here, as for the paper's tailored normal form verifiers, whose canonical decider always receives two answers, a loop reads the pair $(a, a)$ against constraints over two copies of $S_x$ — a one-copy constraint $(c, c_J)$ is the two-copy constraint $(c, 0, c_J)$, and a two-copy constraint $(c_1, c_2, c_J)$ acts as $(c_1 + c_2, c_J)$. And the completeness clauses of the pipeline are read on the doubled game, as Definition [PCC strategy](../../foundations/part-01/def-pcc.md) is read for the existing pipeline: the doubled game is bipartite, so no hypothesis on the verifier is needed to make it synchronous. A ZPC strategy for a game gives one for its doubled game, the same observables at both tags.

- [The trivial strategy; II:1148](lem-tailored-trivial-zpc.md)
- [Signed permutation matrices](lem-signed-perm.md)
- [The Fourier transform; II:974–1006](lem-fourier-pvm.md)
- [Data processing; Claims II:2902 and II:2918](lem-data-processing.md)
- [When a permutation strategy is perfect](lem-perm-strategy-perfect.md)
- [ZPC strategies are PCC strategies](lem-zpc-pcc.md)
- [The Magic Square game; Examples II:1300–1370](prop-magic-square-zpc.md)

## Tailored normal form verifiers

- [Tailored normal form verifier; II:1758](def-tailored-verifier.md)
- [$\lambda$-bounded tailored verifiers, and budgets; II:1800](def-tailored-bounded.md)
- [The canonical decider, as a program; II:1757–1787](def-canonical-decider.md)
- [The canonical decider decides the $n$-th game](lem-canonical-decider.md)
- [A tailored verifier as a normal form verifier; II:1757–1787](def-of-tnfv.md)
- [A tailored verifier and its normal form verifier have the same games](lem-of-tnfv.md)

## The target

- [Tailored game descriptions, standalone; II:1243, II:1279](def-tailored-game-data.md)
- [The tailored halting reduction, as a proposition](def-tailored-halting-reduction.md)
- [$\mathrm{TMIP}^* = \mathrm{RE}$; II:1505, Theorem 7.4 of (BCLV24)](thm-tmip-re.md)
