---
declaration: lemma
origin: cited
lean: MIPRE.QLD.MS.anti, MIPRE.QLD.MS.ms_direct_anticomm, MIPRE.QLD.MS.ms_direct_anticomm', MIPRE.QLD.MS.ms_direct_anticomm_avg, MIPRE.QLD.MS.isPVMIn_repPOVM, MIPRE.QLD.MS.refl_eq_sum, MIPRE.QLD.MS.bnd_one_sub_sq_of_sub, MIPRE.QLD.MS.isometry_πA, MIPRE.QLD.MS.povmValue_swap
statement: formalized
proof: formalized
---

# Direct Magic Square anticommutation — what the pipeline actually needs

Let $|\psi\rangle$ be a unit vector on $\mathbb{C}^{d_\textsc{A}} \otimes \mathbb{C}^{d_\textsc{B}}$ and let $A, B$ be POVM families for the Magic Square game (Definition [LCS game](../../foundations/part-01/def-lcs-game.md) at the magic square's layout), failing it with probability at most $\varepsilon \geq 0$. Write $B_j$ for the second player's $\pm 1$-observable for variable $\textsc{Variable}_j$ — the difference of the two *bit* outcomes, every other answer contributing zero — and $A_j$ for the first player's. If the first player's measurements are projective, then

$$
\left\| { ({I} \otimes \{ B_1, B_5 \}) |\psi\rangle } \right\|^2 \;\leq\; 186624\, \varepsilon\;,
$$

and if the second player's are, then $\left\| { (\{ A_1, A_5 \} \otimes {I}) |\psi\rangle } \right\|^2 \leq 186624\, \varepsilon$, where $\{X, Y\} = XY + YX$. The bound holds on the *original* observables: no isometry, no full Schmidt rank and no extracted EPR pairs are required, and of projectivity only the other player's. It averages without loss: for a family indexed by $\omega$ on the same pair of spaces, the first player's measurements projective, with weights $\nu_\omega \geq 0$, $\sum_\omega \nu_\omega \left\| {({I} \otimes \{B_{1,\omega}, B_{5,\omega}\})|\psi_\omega\rangle} \right\|^2 \leq 186624 \sum_\omega \nu_\omega \varepsilon_\omega$. The Lean proves it for two families of POVMs in the players' algebras of any bipartite model (Definition [Bipartite model](../../downstream-results/part-02/def-bipartite-model.md)) in a unit state; the statement above is its tensor-product instance.

## Depends on

- [The Magic Square](../../foundations/part-01/def-magic-square.md)
- [LCS game](../../foundations/part-01/def-lcs-game.md)

## Proof depends on

- [Generalized Pauli observables in characteristic two](../../foundations/part-02/def-generalized-pauli.md)
- [Bipartite model](../../downstream-results/part-02/def-bipartite-model.md)

## Proof

Repair each of the first player's constraint measurements, sending every outcome that violates the constraint's parity to a fixed parity-valid triple. The repaired measurement is a coarse-graining of a projective measurement, hence projective, and its signed sums are commuting reflections $C_{c,j}$ whose product over a constraint is exactly that constraint's sign. The second player's POVMs are untouched. Uniformity of the $36$ oriented question incidences bounds each conditional loss by $36\varepsilon$, and $\left\| {(C_{c,j} - B_j)|\psi\rangle} \right\|^2 \leq 2 - 2(1 - 2\ell_{c,j}) \leq 4 \ell_{c,j}$ using $C_{c,j}^2 = {I}$ and $B_j^2 \leq {I}$, so $\gamma := \max_{c,j} \left\| {(C_{c,j} - B_j)|\psi\rangle} \right\|$ satisfies $\gamma^2 \leq 144 \varepsilon$.

Write $a, \dots, i$ for Bob's variables $1, \dots, 9$ in row-major order. Substituting one operator at a time costs $\gamma$ each, cross-party products appearing in reversed order, and a constraint relation inserted before a right suffix of length $k$ costs the relation's own $3\gamma$ plus $2k\gamma$. The six-step path

$$
d\,a\,e\,b \;\to\; g\,e\,b \;\to\; g\,h \;\to\; i \;\to\; -f\,c
\;\to\; -d\,e\,c \;\to\; -d\,e\,a\,b\;,
$$

applying the column-one, column-two, row-three, column-three, row-two and row-one constraints in turn, costs $(7 + 3 + 3 + 3 + 5 + 3)\gamma = 24\gamma$, and its two ends give $\left\| { d (ae + ea) b |\psi\rangle } \right\| \leq 24 \gamma$. The sign appears exactly once, at the column-three constraint, which is the one of product $-1$.

Put $R = ae + ea$ and $T = Rb$. Since $\left\| {({I} - B_j^2) W |\psi\rangle} \right\| \leq (2 + k)\gamma$ for a word $W$ of length $k$, the two length-three words in $T$ give $\left\| {({I} - d^2) T |\psi\rangle} \right\| \leq 10\gamma$, and hence $\left\| {T|\psi\rangle} \right\| \leq 34\gamma$. Finally Alice's reflection for variable $2$ commutes with the Bob operator $R$, squares to ${I}$, and approximates $b$ on $|\psi\rangle$ to within $\gamma$, which removes the trailing factor: $\left\| {R |\psi\rangle} \right\| \leq 34\gamma + 2\gamma = 36\gamma$. Squaring and substituting $\gamma^2 \leq 144\varepsilon$ gives $1296 \cdot 144 = 186624$. Exchanging the parties gives Alice's bound. The averaged form is the pointwise bound averaged, with no Jensen step.

## Lean

Formalized as [`MIPRE.QLD.MS.anti`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.MS.anti), [`MIPRE.QLD.MS.ms_direct_anticomm`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.MS.ms_direct_anticomm), [`MIPRE.QLD.MS.ms_direct_anticomm'`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.MS.ms_direct_anticomm'), [`MIPRE.QLD.MS.ms_direct_anticomm_avg`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.MS.ms_direct_anticomm_avg), [`MIPRE.QLD.MS.isPVMIn_repPOVM`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.MS.isPVMIn_repPOVM), [`MIPRE.QLD.MS.refl_eq_sum`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.MS.refl_eq_sum), [`MIPRE.QLD.MS.bnd_one_sub_sq_of_sub`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.MS.bnd_one_sub_sq_of_sub), [`MIPRE.QLD.MS.isometry_πA`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.MS.isometry_πA), [`MIPRE.QLD.MS.povmValue_swap`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.MS.povmValue_swap).

## Sources

- [MIP* = RE blueprint: content/03_background_results.tex, line 449](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/03_background_results.tex#L449)
