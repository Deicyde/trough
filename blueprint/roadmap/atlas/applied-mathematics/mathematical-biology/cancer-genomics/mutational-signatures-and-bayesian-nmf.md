---
declaration: section
origin: cited
lean: Cslib.Bioinformatics.MutationalSignatures.ARDNMF.klDiv, Cslib.Bioinformatics.MutationalSignatures.ARDNMF.recon, Cslib.Bioinformatics.MutationalSignatures.ARDNMF.dataFit, Cslib.Bioinformatics.MutationalSignatures.ARDNMF.objectiveH, Cslib.Bioinformatics.MutationalSignatures.ARDNMF.updateH, Cslib.Bioinformatics.MutationalSignatures.ARDNMF.objectiveH_updateH_le, Cslib.Bioinformatics.MutationalSignatures.ARDNMF.objectiveW, Cslib.Bioinformatics.MutationalSignatures.ARDNMF.updateW
statement: formalized
proof: formalized
---

# Mutational signatures and Bayesian NMF

16 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/cancer-genomics/mutational-signatures-and-bayesian-nmf/index.html).

## Generalized Kullback–Leibler divergence

The Kullback–Leibler `β = 1` divergence `d(x | y) = x log (x / y) - x + y` (Tan–Févotte,
Eq. 4). With Mathlib's `0 * log _ = 0` it gives `d(0 | y) = y`, the correct value; `y > 0` is
needed when `x > 0`.

Formalized by `Cslib.Bioinformatics.MutationalSignatures.ARDNMF.klDiv`, a definition declared in [CSLibExt/Bioinformatics/MutationalSignatures/ARDNMF.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/MutationalSignatures/ARDNMF.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/cancer-genomics/mutational-signatures-and-bayesian-nmf/index.html#kl-div).

## Reconstruction matrix in nonnegative matrix factorization

The reconstruction `(W H)_fn = ∑_k w_fk h_kn`.

Formalized by `Cslib.Bioinformatics.MutationalSignatures.ARDNMF.recon`, a definition declared in [CSLibExt/Bioinformatics/MutationalSignatures/ARDNMF.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/MutationalSignatures/ARDNMF.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/cancer-genomics/mutational-signatures-and-bayesian-nmf/index.html#recon).

## Data-fit term of the ARD-NMF objective

The data-fit term `D_1(V | W H) = ∑_{f,n} d(v_fn | (W H)_fn)`.

Formalized by `Cslib.Bioinformatics.MutationalSignatures.ARDNMF.dataFit`, a definition declared in [CSLibExt/Bioinformatics/MutationalSignatures/ARDNMF.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/MutationalSignatures/ARDNMF.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/cancer-genomics/mutational-signatures-and-bayesian-nmf/index.html#data-fit).

## H-dependent part of the ARD-NMF objective

The `H`-dependent part `D_1(V | W H) / φ + ∑_{k,n} h_kn / λ_k` of the `ℓ₁`-ARD objective
(Tan–Févotte, Eq. 20, `β = 1`).

Formalized by `Cslib.Bioinformatics.MutationalSignatures.ARDNMF.objectiveH`, a definition declared in [CSLibExt/Bioinformatics/MutationalSignatures/ARDNMF.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/MutationalSignatures/ARDNMF.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/cancer-genomics/mutational-signatures-and-bayesian-nmf/index.html#objective-h).

## ARD multiplicative update of H

The `ℓ₁`-ARD multiplicative update of `H` for `β = 1` (Tan–Févotte, Eq. 32, Algorithm 2):
`h_kn ← h_kn (∑_f w_fk v_fn / (W H)_fn) / (∑_f w_fk + φ / λ_k)`.

Formalized by `Cslib.Bioinformatics.MutationalSignatures.ARDNMF.updateH`, a definition declared in [CSLibExt/Bioinformatics/MutationalSignatures/ARDNMF.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/MutationalSignatures/ARDNMF.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/cancer-genomics/mutational-signatures-and-bayesian-nmf/index.html#update-h).

## The `H` update is monotone

**The `H` update is monotone** (Tan–Févotte 2013, §IV-B, `β = 1`): it does not increase
`D_1(V | W H) / φ + ∑ h_kn / λ_k`, for `φ > 0`, `λ > 0`, `V ≥ 0`, `W ≥ 0` with no zero row, and
`H > 0` entrywise.

Formalized by `Cslib.Bioinformatics.MutationalSignatures.ARDNMF.objectiveH_updateH_le`, a theorem declared in [CSLibExt/Bioinformatics/MutationalSignatures/ARDNMF.lean, line 244](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/MutationalSignatures/ARDNMF.lean#L244). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/cancer-genomics/mutational-signatures-and-bayesian-nmf/index.html#objective-h-update-h-le).

## W-dependent part of the ARD-NMF objective

The `W`-dependent part `D_1(V | W H) / φ + ∑_{f,k} w_fk / λ_k` of the `ℓ₁`-ARD objective
(Tan–Févotte, Eq. 20, `β = 1`).

Formalized by `Cslib.Bioinformatics.MutationalSignatures.ARDNMF.objectiveW`, a definition declared in [CSLibExt/Bioinformatics/MutationalSignatures/ARDNMF.lean, line 276](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/MutationalSignatures/ARDNMF.lean#L276). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/cancer-genomics/mutational-signatures-and-bayesian-nmf/index.html#objective-w).

## ARD multiplicative update of W

The `ℓ₁`-ARD multiplicative update of `W` for `β = 1` (Tan–Févotte, Algorithm 2):
`w_fk ← w_fk (∑_n v_fn h_kn / (W H)_fn) / (∑_n h_kn + φ / λ_k)`.

Formalized by `Cslib.Bioinformatics.MutationalSignatures.ARDNMF.updateW`, a definition declared in [CSLibExt/Bioinformatics/MutationalSignatures/ARDNMF.lean, line 282](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/MutationalSignatures/ARDNMF.lean#L282). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/cancer-genomics/mutational-signatures-and-bayesian-nmf/index.html#update-w).

## The `W` update is monotone

It does not increase
`D_1(V | W H) / φ + ∑ w_fk / λ_k`, for `φ > 0`, `λ > 0`, `V ≥ 0`, `H ≥ 0` with no zero column,
and `W > 0` entrywise (the transpose of `objectiveH_updateH_le`).

Formalized by `Cslib.Bioinformatics.MutationalSignatures.ARDNMF.objectiveW_updateW_le`, a theorem declared in [CSLibExt/Bioinformatics/MutationalSignatures/ARDNMF.lean, line 289](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/MutationalSignatures/ARDNMF.lean#L289). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/cancer-genomics/mutational-signatures-and-bayesian-nmf/index.html#objective-w-update-w-le).

## Relevance update in ARD-NMF

The relevance update `λ_k = (‖w_k‖₁ + ‖h_k‖₁ + b) / c` (Tan–Févotte, Eq. 33, `ℓ₁` prior;
`c = F + N + a + 1`).

Formalized by `Cslib.Bioinformatics.MutationalSignatures.ARDNMF.relevance`, a definition declared in [CSLibExt/Bioinformatics/MutationalSignatures/ARDNMF.lean, line 325](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/MutationalSignatures/ARDNMF.lean#L325). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/cancer-genomics/mutational-signatures-and-bayesian-nmf/index.html#relevance).

## The relevance update is the exact minimizer

**The relevance update is the exact minimizer** (Tan–Févotte, §IV-C): for `A > 0` and
`c > 0`, `λ ↦ A / λ + c log λ` attains its minimum over `λ > 0` at `λ = A / c`.

Formalized by `Cslib.Bioinformatics.MutationalSignatures.ARDNMF.relevance_isMinOn`, a theorem declared in [CSLibExt/Bioinformatics/MutationalSignatures/ARDNMF.lean, line 330](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/MutationalSignatures/ARDNMF.lean#L330). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/cancer-genomics/mutational-signatures-and-bayesian-nmf/index.html#relevance-is-min-on).

## The minimizer is unique

If `λ > 0` does as well as `A / c`, then `λ = A / c`.

Formalized by `Cslib.Bioinformatics.MutationalSignatures.ARDNMF.relevance_unique`, a theorem declared in [CSLibExt/Bioinformatics/MutationalSignatures/ARDNMF.lean, line 345](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/MutationalSignatures/ARDNMF.lean#L345). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/cancer-genomics/mutational-signatures-and-bayesian-nmf/index.html#relevance-unique).

## Lower bound on the relevance update

The relevance never falls below its floor `b / c` (`W, H ≥ 0`, `c > 0`).

Formalized by `Cslib.Bioinformatics.MutationalSignatures.ARDNMF.div_le_relevance`, a theorem declared in [CSLibExt/Bioinformatics/MutationalSignatures/ARDNMF.lean, line 365](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/MutationalSignatures/ARDNMF.lean#L365). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/cancer-genomics/mutational-signatures-and-bayesian-nmf/index.html#div-le-relevance).

## Pruning

**Pruning** (Tan–Févotte, §IV-D): the relevance equals its floor `b / c` exactly when the
`k`-th column of `W` and the `k`-th row of `H` are zero (`W, H ≥ 0`, `c > 0`).

Formalized by `Cslib.Bioinformatics.MutationalSignatures.ARDNMF.relevance_eq_floor_iff`, a theorem declared in [CSLibExt/Bioinformatics/MutationalSignatures/ARDNMF.lean, line 376](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/MutationalSignatures/ARDNMF.lean#L376). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/cancer-genomics/mutational-signatures-and-bayesian-nmf/index.html#relevance-eq-floor-iff).

## A pruned entry stays pruned

The multiplicative update maps a zero entry of `H` to
zero.

Formalized by `Cslib.Bioinformatics.MutationalSignatures.ARDNMF.updateH_eq_zero`, a theorem declared in [CSLibExt/Bioinformatics/MutationalSignatures/ARDNMF.lean, line 396](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/MutationalSignatures/ARDNMF.lean#L396). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/cancer-genomics/mutational-signatures-and-bayesian-nmf/index.html#update-h-eq-zero).

## A pruned entry stays pruned

The multiplicative update maps a zero entry of `W` to
zero.

Formalized by `Cslib.Bioinformatics.MutationalSignatures.ARDNMF.updateW_eq_zero`, a theorem declared in [CSLibExt/Bioinformatics/MutationalSignatures/ARDNMF.lean, line 403](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/MutationalSignatures/ARDNMF.lean#L403). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/cancer-genomics/mutational-signatures-and-bayesian-nmf/index.html#update-w-eq-zero).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Mutational signatures and Bayesian NMF](https://deicyde.github.io/atlas-lean/roadmap/Biology/cancer-genomics/mutational-signatures-and-bayesian-nmf/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Biology/cancer-genomics/mutational-signatures-and-bayesian-nmf)
