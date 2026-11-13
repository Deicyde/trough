---
declaration: section
origin: cited
lean: MathlibExt.Biology.Phylogenetics.SubstitutionModels.gtrRate, MathlibExt.Biology.Phylogenetics.SubstitutionModels.sum_gtrRate, MathlibExt.Biology.Phylogenetics.SubstitutionModels.isRateMatrix_gtrRate, MathlibExt.Biology.Phylogenetics.SubstitutionModels.isDetailedBalance_gtrRate, MathlibExt.Biology.Phylogenetics.SubstitutionModels.vecMul_gtrRate, MathlibExt.Biology.Phylogenetics.SubstitutionModels.vecMul_ctmcTransition_gtrRate, MathlibExt.Biology.Phylogenetics.SubstitutionModels.isDetailedBalance_ctmcTransition_gtrRate, MathlibExt.Biology.Phylogenetics.SubstitutionModels.hkyExchangeability
statement: formalized
proof: formalized
---

# Time-reversible nucleotide substitution models

21 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/time-reversible-nucleotide-substitution-models/index.html).

## General time-reversible (GTR) rate matrix

The **GTR rate matrix** (Tavaré 1986) with base frequencies `π` and exchangeabilities `s`:
`s i j * π j` off the diagonal and minus the off-diagonal row sum on it. The diagonal of `s` is
not used.

Formalized by `MathlibExt.Biology.Phylogenetics.SubstitutionModels.gtrRate`, a definition declared in [MathlibExt/Biology/Phylogenetics/SubstitutionModels.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Phylogenetics/SubstitutionModels.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/time-reversible-nucleotide-substitution-models/index.html#gtr-rate).

## Rows of the GTR rate matrix sum to zero

The rows of the GTR matrix sum to `0`, for all parameters.

Formalized by `MathlibExt.Biology.Phylogenetics.SubstitutionModels.sum_gtrRate`, a theorem declared in [MathlibExt/Biology/Phylogenetics/SubstitutionModels.lean, line 93](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Phylogenetics/SubstitutionModels.lean#L93). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/time-reversible-nucleotide-substitution-models/index.html#sum-gtr-rate).

## GTR matrix is a rate matrix

With nonnegative base frequencies and nonnegative off-diagonal exchangeabilities, the GTR
matrix is a rate matrix (the diagonal `s i i` is not used by `gtrRate`).

Formalized by `MathlibExt.Biology.Phylogenetics.SubstitutionModels.isRateMatrix_gtrRate`, a theorem declared in [MathlibExt/Biology/Phylogenetics/SubstitutionModels.lean, line 101](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Phylogenetics/SubstitutionModels.lean#L101). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/time-reversible-nucleotide-substitution-models/index.html#is-rate-matrix-gtr-rate).

## GTR is reversible

With symmetric exchangeabilities, the GTR matrix is in detailed
balance with its base frequencies, `π i Q i j = π j Q j i` (Tavaré 1986).

Formalized by `MathlibExt.Biology.Phylogenetics.SubstitutionModels.isDetailedBalance_gtrRate`, a theorem declared in [MathlibExt/Biology/Phylogenetics/SubstitutionModels.lean, line 108](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Phylogenetics/SubstitutionModels.lean#L108). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/time-reversible-nucleotide-substitution-models/index.html#is-detailed-balance-gtr-rate).

## Base frequencies are invariant for the GTR generator

The base frequencies are invariant for the GTR generator: `π Q = 0`.

Formalized by `MathlibExt.Biology.Phylogenetics.SubstitutionModels.vecMul_gtrRate`, a theorem declared in [MathlibExt/Biology/Phylogenetics/SubstitutionModels.lean, line 119](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Phylogenetics/SubstitutionModels.lean#L119). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/time-reversible-nucleotide-substitution-models/index.html#vec-mul-gtr-rate).

## Base frequencies are stationary for the GTR chain

The base frequencies are stationary for the GTR transition function at every time.

Formalized by `MathlibExt.Biology.Phylogenetics.SubstitutionModels.vecMul_ctmcTransition_gtrRate`, a theorem declared in [MathlibExt/Biology/Phylogenetics/SubstitutionModels.lean, line 124](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Phylogenetics/SubstitutionModels.lean#L124). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/time-reversible-nucleotide-substitution-models/index.html#vec-mul-ctmc-transition-gtr-rate).

## Time-reversibility of the GTR chain

Detailed balance of the GTR transition function with the base frequencies,
`π i P t i j = π j P t j i` for every `t` (time-reversibility of the GTR chain).

Formalized by `MathlibExt.Biology.Phylogenetics.SubstitutionModels.isDetailedBalance_ctmcTransition_gtrRate`, a theorem declared in [MathlibExt/Biology/Phylogenetics/SubstitutionModels.lean, line 130](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Phylogenetics/SubstitutionModels.lean#L130). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/time-reversible-nucleotide-substitution-models/index.html#is-detailed-balance-ctmc-transition-gtr).

## HKY85 exchangeabilities

The HKY85 exchangeabilities: `κ` for a transition (indices of equal parity: `A ↔ G`,
`C ↔ T` in the order `A, C, G, T`), `1` for a transversion. The diagonal (also `κ`) is not
used by `gtrRate`.

Formalized by `MathlibExt.Biology.Phylogenetics.SubstitutionModels.hkyExchangeability`, a definition declared in [MathlibExt/Biology/Phylogenetics/SubstitutionModels.lean, line 140](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Phylogenetics/SubstitutionModels.lean#L140). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/time-reversible-nucleotide-substitution-models/index.html#hky-exchangeability).

## HKY85 rate matrix

The **HKY85 rate matrix** (Hasegawa–Kishino–Yano 1985) with base frequencies `π` and
transition/transversion ratio `κ`: rate `κ π j` for a transition to `j`, `π j` for a
transversion.

Formalized by `MathlibExt.Biology.Phylogenetics.SubstitutionModels.hkyRate`, a definition declared in [MathlibExt/Biology/Phylogenetics/SubstitutionModels.lean, line 146](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Phylogenetics/SubstitutionModels.lean#L146). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/time-reversible-nucleotide-substitution-models/index.html#hky-rate).

## F81 rate matrix

The **F81 rate matrix** (Felsenstein 1981): rate `π j` to every other base `j`.

Formalized by `MathlibExt.Biology.Phylogenetics.SubstitutionModels.f81Rate`, a definition declared in [MathlibExt/Biology/Phylogenetics/SubstitutionModels.lean, line 150](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Phylogenetics/SubstitutionModels.lean#L150). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/time-reversible-nucleotide-substitution-models/index.html#f81-rate).

## K80 rate matrix

The **K80 rate matrix** (Kimura 1980): equal base frequencies `1/4`, rate `κ / 4` for a
transition and `1 / 4` for each transversion.

Formalized by `MathlibExt.Biology.Phylogenetics.SubstitutionModels.k80Rate`, a definition declared in [MathlibExt/Biology/Phylogenetics/SubstitutionModels.lean, line 155](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Phylogenetics/SubstitutionModels.lean#L155). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/time-reversible-nucleotide-substitution-models/index.html#k80-rate).

## HKY85 matrix is a rate matrix

With nonnegative base frequencies and `κ ≥ 0`, the HKY85 matrix is a rate matrix.

Formalized by `MathlibExt.Biology.Phylogenetics.SubstitutionModels.isRateMatrix_hkyRate`, a theorem declared in [MathlibExt/Biology/Phylogenetics/SubstitutionModels.lean, line 159](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Phylogenetics/SubstitutionModels.lean#L159). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/time-reversible-nucleotide-substitution-models/index.html#is-rate-matrix-hky-rate).

## F81 matrix is a rate matrix

With nonnegative base frequencies, the F81 matrix is a rate matrix.

Formalized by `MathlibExt.Biology.Phylogenetics.SubstitutionModels.isRateMatrix_f81Rate`, a theorem declared in [MathlibExt/Biology/Phylogenetics/SubstitutionModels.lean, line 166](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Phylogenetics/SubstitutionModels.lean#L166). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/time-reversible-nucleotide-substitution-models/index.html#is-rate-matrix-f81-rate).

## K80 matrix is a rate matrix

With `κ ≥ 0`, the K80 matrix is a rate matrix.

Formalized by `MathlibExt.Biology.Phylogenetics.SubstitutionModels.isRateMatrix_k80Rate`, a theorem declared in [MathlibExt/Biology/Phylogenetics/SubstitutionModels.lean, line 170](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Phylogenetics/SubstitutionModels.lean#L170). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/time-reversible-nucleotide-substitution-models/index.html#is-rate-matrix-k80-rate).

## Detailed balance of the HKY85 model

HKY85 is in detailed balance with its base frequencies.

Formalized by `MathlibExt.Biology.Phylogenetics.SubstitutionModels.isDetailedBalance_hkyRate`, a theorem declared in [MathlibExt/Biology/Phylogenetics/SubstitutionModels.lean, line 174](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Phylogenetics/SubstitutionModels.lean#L174). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/time-reversible-nucleotide-substitution-models/index.html#is-detailed-balance-hky-rate).

## Detailed balance of the F81 model

F81 is in detailed balance with its base frequencies.

Formalized by `MathlibExt.Biology.Phylogenetics.SubstitutionModels.isDetailedBalance_f81Rate`, a theorem declared in [MathlibExt/Biology/Phylogenetics/SubstitutionModels.lean, line 180](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Phylogenetics/SubstitutionModels.lean#L180). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/time-reversible-nucleotide-substitution-models/index.html#is-detailed-balance-f81-rate).

## HKY85 with κ = 1 is F81

HKY85 with `κ = 1` is F81.

Formalized by `MathlibExt.Biology.Phylogenetics.SubstitutionModels.hkyRate_one`, a theorem declared in [MathlibExt/Biology/Phylogenetics/SubstitutionModels.lean, line 184](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Phylogenetics/SubstitutionModels.lean#L184). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/time-reversible-nucleotide-substitution-models/index.html#hky-rate-one).

## JC69 is the equal-rates GTR model

Equal base frequencies `1/4` and equal
exchangeabilities `4 μ / 3` give the Jukes–Cantor rate matrix `jcRateMatrix μ`.

Formalized by `MathlibExt.Biology.Phylogenetics.SubstitutionModels.gtrRate_jukesCantor`, a theorem declared in [MathlibExt/Biology/Phylogenetics/SubstitutionModels.lean, line 192](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Phylogenetics/SubstitutionModels.lean#L192). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/time-reversible-nucleotide-substitution-models/index.html#gtr-rate-jukes-cantor).

## Equal-rates GTR chain is the Jukes–Cantor model

The equal-rates GTR transition function is the Jukes–Cantor transition probability
`jcProb μ t` (by `JukesCantor.jcProb_eq_exp`).

Formalized by `MathlibExt.Biology.Phylogenetics.SubstitutionModels.ctmcTransition_gtrRate_jukesCantor`, a theorem declared in [MathlibExt/Biology/Phylogenetics/SubstitutionModels.lean, line 204](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Phylogenetics/SubstitutionModels.lean#L204). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/time-reversible-nucleotide-substitution-models/index.html#ctmc-transition-gtr-rate-jukes-cantor).

## Jukes–Cantor matrix is a rate matrix

For `μ ≥ 0` the Jukes–Cantor matrix is a rate matrix.

Formalized by `MathlibExt.Biology.Phylogenetics.SubstitutionModels.isRateMatrix_jcRateMatrix`, a theorem declared in [MathlibExt/Biology/Phylogenetics/SubstitutionModels.lean, line 212](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Phylogenetics/SubstitutionModels.lean#L212). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/time-reversible-nucleotide-substitution-models/index.html#is-rate-matrix-jc-rate-matrix).

## K80 with κ = 1 is the Jukes–Cantor model

K80 with `κ = 1` is JC69 with substitution rate `μ = 3/4`.

Formalized by `MathlibExt.Biology.Phylogenetics.SubstitutionModels.k80Rate_one`, a theorem declared in [MathlibExt/Biology/Phylogenetics/SubstitutionModels.lean, line 216](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Phylogenetics/SubstitutionModels.lean#L216). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/time-reversible-nucleotide-substitution-models/index.html#k80-rate-one).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Time-reversible nucleotide substitution models](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/time-reversible-nucleotide-substitution-models/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Biology/phylogenetics/time-reversible-nucleotide-substitution-models)
