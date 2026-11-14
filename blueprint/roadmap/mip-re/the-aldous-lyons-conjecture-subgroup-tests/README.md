# The Aldous–Lyons conjecture: subgroup tests

This chapter is the plan and the progress of Phase 6 of `planning/aldous-lyons-track.md`: the companion paper (BCLV24) of Bowen, Chapman, Lubotzky and Vidick, which with Chapter [The Aldous–Lyons track: $\mathrm{TMIP}^* = \mathrm{RE}$](../the-aldous-lyons-track-tmip-re/README.md) refutes the Aldous–Lyons conjecture. Line numbers I:$n$ refer to the LaTeX source of its arXiv version, which is the authority on the mathematics. Its argument has two halves. Main Theorem II (Theorem I:2126), finitary, associates with a tailored game a subgroup test whose sofic value is $1$ when the game has a perfect ZPC strategy and bounded away from $1$ when the game's value is at most $\frac12$. Main Theorem I (I:594) shows that under the conjecture the sofic value is approximable by a computable function. Together with a halting reduction to tailored games they contradict the undecidability of the halting problem.

*Status.* The definitions are formalized (`MIPRE/SubgroupTestValue.lean`, self-contained, and `MIPRE/Tailored/Sofic/`): subgroup tests and their sofic value, the Aldous–Lyons conjecture, and the associated test of a tailored game. Proved: the associated test is computable from the game (Lemma [The associated test is computable from the game](part-01/lem-assoc-test-primrec.md)), and Main Theorem II with a halting reduction makes the sofic value not approximable (Theorem [The sofic value is not approximable; Corollary I:2144, measure-free](part-01/thm-sofic-not-approximable.md)); and the perturbation half of Main Theorem II's soundness (Proposition [Perturbing to pass Checks 1–3; Proposition I:2267](part-01/prop-assoc-perturb.md)); Main Theorem II itself (Theorem [Main Theorem II; Theorem I:2126](part-01/thm-main-theorem-ii.md)); and so the sofic value is not approximable from a halting reduction to tailored games (Corollary [The sofic value is not approximable, from tailored answer reduction](part-01/cor-sofic-not-approximable-ar.md)). Main Theorem I (Theorems [Main Theorem I (1): the sofic value is approximable from below; I:594](part-02/thm-main-theorem-i-lower.md) and [Main Theorem I (2): the ergodic value is approximable from above; I:594](part-02/thm-main-theorem-i-upper.md)) is formalized too, so the Aldous–Lyons conjecture is false from a halting reduction to tailored games, and from a tailored answer reduction (Corollary [The Aldous–Lyons conjecture is false, from tailored answer reduction](part-02/cor-aldous-lyons-false-ar.md)). Paper II's main theorem is proved (Theorem [$\mathrm{TMIP}^* = \mathrm{RE}$; II:1505, Theorem 7.4 of (BCLV24)](../the-aldous-lyons-track-tmip-re/part-01/thm-tmip-re.md)), so the conjecture is false (Corollary [The Aldous–Lyons conjecture is false](part-02/cor-aldous-lyons-false-final.md)).

## Subgroup tests and the conjecture

## [Subgroup tests and their sofic… to The value of a measure, and the…](part-01/README.md)

- [Subgroup tests and their sofic value; I:439–520](part-01/def-subgroup-test.md)
- [Approximating the sofic value](part-01/def-sofic-approximable.md)
- [Invariant random subgroups and the Aldous–Lyons conjecture; I:467–530](part-01/def-aldous-lyons.md)
- [The associated subgroup test; I:2086](part-01/def-assoc-test.md)
- [The associated test is computable from the game](part-01/lem-assoc-test-primrec.md)
- [Hamming distance of permutations](part-01/lem-perm-hamming.md)
- [Stability of involutions, fixed-point-free involutions and commuting families; I:2561–2649](part-01/lem-perm-stability.md)
- [Robustness of the value; Claim I:1480](part-01/lem-test-robust.md)
- [Significance of the associated test; Proposition I:2283](part-01/lem-assoc-significance.md)
- [Perturbing to pass Checks 1–3; Proposition I:2267](part-01/prop-assoc-perturb.md)
- [Z-aligned signed-permutation strategies without commutation along edges](part-01/def-zstrat.md)
- [The trace identity](part-01/lem-trace-identity.md)
- [Passing a challenge under Checks 1–3](part-01/lem-assoc-passes.md)
- [The quotient by $J$](part-01/lem-j-quotient.md)
- [Game value of an action passing Checks 1–3; Proposition I:2279](part-01/prop-checks-game-value.md)
- [Completeness: lifting a perfect strategy; Theorem I:2126 (1)](part-01/lem-assoc-completeness.md)
- [Main Theorem II; Theorem I:2126](part-01/thm-main-theorem-ii.md)
- [The sofic value is not approximable, from tailored answer reduction](part-01/cor-sofic-not-approximable-ar.md)
- [The sofic value is not approximable; Corollary I:2144, measure-free](part-01/thm-sofic-not-approximable.md)
- [The value of a measure, and the ergodic value; I:486–499](part-01/def-erg-value.md)

## [The value is a continuous… to The Aldous–Lyons conjecture is…](part-02/README.md)

- [The value is a continuous functional; I:550](part-02/lem-val-on-continuous.md)
- [The sofic value is at most the ergodic value, with equality under Aldous–Lyons; Corollary I:550](part-02/cor-sof-eq-erg.md)
- [Main Theorem I (1): the sofic value is approximable from below; I:594](part-02/thm-main-theorem-i-lower.md)
- [From word indicators to invariant random subgroups](part-02/lem-irs-of-good.md)
- [Pseudo-subgroup polytopes, discretized; I:927, I:1105](part-02/def-pseudo-subgroup-polytope.md)
- [The upper value bounds the ergodic value](part-02/lem-erg-le-upper.md)
- [The upper value converges to the ergodic value](part-02/lem-upper-converge.md)
- [Main Theorem I (2): the ergodic value is approximable from above; I:594](part-02/thm-main-theorem-i-upper.md)
- [Aldous–Lyons makes the sofic value approximable; Corollary I:605](part-02/cor-al-sof-approximable.md)
- [The Aldous–Lyons conjecture is false; Corollary I:2144](part-02/thm-aldous-lyons-false.md)
- [The Aldous–Lyons conjecture is false, from tailored answer reduction](part-02/cor-aldous-lyons-false-ar.md)
- [The Aldous–Lyons conjecture is false](part-02/cor-aldous-lyons-false-final.md)
