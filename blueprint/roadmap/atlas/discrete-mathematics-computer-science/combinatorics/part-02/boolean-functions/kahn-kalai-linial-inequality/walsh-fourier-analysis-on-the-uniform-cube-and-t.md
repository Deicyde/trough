---
declaration: section
origin: cited
lean: StatMech.Probability.khc_sign, StatMech.Probability.khc_walshChar, StatMech.Probability.khc_fourierCoeff, StatMech.Probability.khc_reindex, StatMech.Probability.khc_cubeEquiv, StatMech.Probability.khc_walshChar_eq_cubeChi, StatMech.Probability.khc_fourierCoeff_eq_boolFourierCoeff, StatMech.Probability.khc_walshChar_reindex
statement: formalized
proof: formalized
---

# Walsh–Fourier analysis on the uniform cube and the KKL reduction

23 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/walsh-fourier-analysis-on-the-uniform-cube-and-t/index.html).

## $\pm 1$ value of a bit

The `±1` value of a bit: `false ↦ 1`, `true ↦ -1`.

Formalized by `StatMech.Probability.khc_sign`, a definition declared in [CSLibExt/Complexity/BooleanFunctions/KKL/KKLfromHC.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Complexity/BooleanFunctions/KKL/KKLfromHC.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/walsh-fourier-analysis-on-the-uniform-cube-and-t/index.html#khc-sign).

## Walsh character on the Boolean cube

The Walsh character `χ_S(x) = ∏_{i ∈ S} (-1)^{x i}` on `{0, 1}^ι`.

This legacy sign convention is retained for KKL consumers; its proofs use
 `BooleanCube.cubeChi` through `khc_walshChar_eq_cubeChi`.

Formalized by `StatMech.Probability.khc_walshChar`, a definition declared in [CSLibExt/Complexity/BooleanFunctions/KKL/KKLfromHC.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Complexity/BooleanFunctions/KKL/KKLfromHC.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/walsh-fourier-analysis-on-the-uniform-cube-and-t/index.html#khc-walsh-char).

## Fourier–Walsh coefficient under the uniform measure

The Fourier–Walsh coefficient `f̂(S) = 𝔼[f χ_S]` under the uniform measure.

This retains the legacy signs; `khc_fourierCoeff_eq_boolFourierCoeff` transports
 the canonical Fourier identities used below.

Formalized by `StatMech.Probability.khc_fourierCoeff`, a definition declared in [CSLibExt/Complexity/BooleanFunctions/KKL/KKLfromHC.lean, line 116](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Complexity/BooleanFunctions/KKL/KKLfromHC.lean#L116). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/walsh-fourier-analysis-on-the-uniform-cube-and-t/index.html#khc-fourier-coeff).

## Reindexing a cube function along an index bijection

The function `f` on `{0, 1}^ι` transported to `{0, 1}^κ` along the bijection `e : κ ≃ ι`.

Formalized by `StatMech.Probability.khc_reindex`, a definition declared in [CSLibExt/Complexity/BooleanFunctions/KKL/KKLfromHC.lean, line 120](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Complexity/BooleanFunctions/KKL/KKLfromHC.lean#L120). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/walsh-fourier-analysis-on-the-uniform-cube-and-t/index.html#khc-reindex).

## Cube bijection induced by an index bijection

The bijection `{0, 1}^ι ≃ {0, 1}^κ` induced by `e : κ ≃ ι`.

Formalized by `StatMech.Probability.khc_cubeEquiv`, a definition declared in [CSLibExt/Complexity/BooleanFunctions/KKL/KKLfromHC.lean, line 125](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Complexity/BooleanFunctions/KKL/KKLfromHC.lean#L125). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/walsh-fourier-analysis-on-the-uniform-cube-and-t/index.html#khc-cube-equiv).

## Walsh character agrees with the canonical cube character up to sign

On `Fin n`, the Walsh character is `BooleanCube.cubeChi` up to the sign `(-1)^{|S|}`:
`BooleanCube.cubeVal` sends `true` to `1`, while `khc_sign` sends it to `-1`.

Formalized by `StatMech.Probability.khc_walshChar_eq_cubeChi`, a theorem declared in [CSLibExt/Complexity/BooleanFunctions/KKL/KKLfromHC.lean, line 170](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Complexity/BooleanFunctions/KKL/KKLfromHC.lean#L170). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/walsh-fourier-analysis-on-the-uniform-cube-and-t/index.html#khc-walsh-char-eq-cube-chi).

## Walsh coefficient is the canonical Fourier coefficient up to sign

On `Fin n`, the Fourier coefficient is `BooleanCube.boolFourierCoeff` up to the sign
`(-1)^{|S|}`.

Formalized by `StatMech.Probability.khc_fourierCoeff_eq_boolFourierCoeff`, a theorem declared in [CSLibExt/Complexity/BooleanFunctions/KKL/KKLfromHC.lean, line 179](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Complexity/BooleanFunctions/KKL/KKLfromHC.lean#L179). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/walsh-fourier-analysis-on-the-uniform-cube-and-t/index.html#khc-fourier-coeff-eq-bool-fourier-coeff).

## Reindexing a Walsh character reindexes its coordinate set

Reindexing a Walsh character reindexes its finite set of coordinates.

Formalized by `StatMech.Probability.khc_walshChar_reindex`, a theorem declared in [CSLibExt/Complexity/BooleanFunctions/KKL/KKLfromHC.lean, line 191](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Complexity/BooleanFunctions/KKL/KKLfromHC.lean#L191). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/walsh-fourier-analysis-on-the-uniform-cube-and-t/index.html#khc-walsh-char-reindex).

## Reindexing preserves values at corresponding cube points

Reindexing back at the corresponding cube point recovers the original value.

Formalized by `StatMech.Probability.khc_reindex_cubeEquiv`, a theorem declared in [CSLibExt/Complexity/BooleanFunctions/KKL/KKLfromHC.lean, line 198](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Complexity/BooleanFunctions/KKL/KKLfromHC.lean#L198). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/walsh-fourier-analysis-on-the-uniform-cube-and-t/index.html#khc-reindex-cube-equiv).

## Fourier coefficients are invariant under reindexing

Fourier coefficients are unchanged when both the function and its index are reindexed.

Formalized by `StatMech.Probability.khc_fourierCoeff_reindex`, a theorem declared in [CSLibExt/Complexity/BooleanFunctions/KKL/KKLfromHC.lean, line 203](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Complexity/BooleanFunctions/KKL/KKLfromHC.lean#L203). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/walsh-fourier-analysis-on-the-uniform-cube-and-t/index.html#khc-fourier-coeff-reindex).

## Fourier inversion on the Boolean cube

Fourier inversion: `f = ∑_S f̂(S) χ_S`.

Formalized by `StatMech.Probability.khc_fourier_expansion`, a theorem declared in [CSLibExt/Complexity/BooleanFunctions/KKL/KKLfromHC.lean, line 267](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Complexity/BooleanFunctions/KKL/KKLfromHC.lean#L267). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/walsh-fourier-analysis-on-the-uniform-cube-and-t/index.html#khc-fourier-expansion).

## Parseval's identity on the Boolean cube

Parseval's identity: `𝔼[f g] = ∑_S f̂(S) ĝ(S)`.

Transported from `BooleanCube.expect_mul_eq_sum_boolFourierCoeff_mul`.

Formalized by `StatMech.Probability.khc_parseval`, a theorem declared in [CSLibExt/Complexity/BooleanFunctions/KKL/KKLfromHC.lean, line 293](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Complexity/BooleanFunctions/KKL/KKLfromHC.lean#L293). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/walsh-fourier-analysis-on-the-uniform-cube-and-t/index.html#khc-parseval).

## Noise operator is diagonal in the Walsh basis

The noise operator acts diagonally on the Walsh basis: `T_ρ f = ∑_S ρ^{|S|} f̂(S) χ_S`.

Transported from `BooleanCube.boolNoiseOp_eq_sum`, for every real `ρ`.

Formalized by `StatMech.Probability.khc_noiseOp_fourier`, a theorem declared in [CSLibExt/Complexity/BooleanFunctions/KKL/KKLfromHC.lean, line 347](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Complexity/BooleanFunctions/KKL/KKLfromHC.lean#L347). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/walsh-fourier-analysis-on-the-uniform-cube-and-t/index.html#khc-noise-op-fourier).

## Bonami–Beckner hypercontractive inequality

**Bonami–Beckner hypercontractive inequality** (A. Bonami, *Étude des coefficients de Fourier
 des fonctions de Lᵖ(G)*, Ann. Inst. Fourier 1970; W. Beckner, *Inequalities in Fourier
 analysis*, Ann. of Math. 1975): `‖T_ρ g‖₂ ≤ ‖g‖_{1+ρ²}` on `{0, 1}^ι` for `0 ≤ ρ ≤ 1`.

Formalized by `StatMech.Probability.khc_hypercontractivity_general`, a theorem declared in [CSLibExt/Complexity/BooleanFunctions/KKL/KKLfromHC.lean, line 384](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Complexity/BooleanFunctions/KKL/KKLfromHC.lean#L384). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/walsh-fourier-analysis-on-the-uniform-cube-and-t/index.html#khc-hypercontractivity-general).

## Hypercontractivity in Fourier form

Hypercontractivity in Fourier form: `∑_S ρ^{2|S|} f̂(S)² ≤ ‖f‖²_{1+ρ²}`.

Formalized by `StatMech.Probability.khc_lowDegreeWeight_le`, a theorem declared in [CSLibExt/Complexity/BooleanFunctions/KKL/KKLfromHC.lean, line 395](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Complexity/BooleanFunctions/KKL/KKLfromHC.lean#L395). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/walsh-fourier-analysis-on-the-uniform-cube-and-t/index.html#khc-low-degree-weight-le).

## Variance as Fourier weight off the empty set

Variance under the uniform measure is the Fourier weight off the empty set.

Formalized by `StatMech.Probability.khc_var_eq_fourierWeight`, a theorem declared in [CSLibExt/Complexity/BooleanFunctions/KKL/KKLfromHC.lean, line 448](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Complexity/BooleanFunctions/KKL/KKLfromHC.lean#L448). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/walsh-fourier-analysis-on-the-uniform-cube-and-t/index.html#khc-var-eq-fourier-weight).

## Event influence is four times the canonical influence

Event influence is four times canonical quarter-square influence after reindexing.

Formalized by `StatMech.Probability.khc_infl_eq_four_boolInfluence`, a theorem declared in [CSLibExt/Complexity/BooleanFunctions/KKL/KKLfromHC.lean, line 562](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Complexity/BooleanFunctions/KKL/KKLfromHC.lean#L562). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/walsh-fourier-analysis-on-the-uniform-cube-and-t/index.html#khc-infl-eq-four-bool-influence).

## Influence of a coordinate as Fourier weight

The influence of `e` on a Boolean function is `∑_{S ∋ e} 4 f̂(S)²`.

Formalized by `StatMech.Probability.khc_infl_eq_fourierWeight`, a theorem declared in [CSLibExt/Complexity/BooleanFunctions/KKL/KKLfromHC.lean, line 605](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Complexity/BooleanFunctions/KKL/KKLfromHC.lean#L605). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/walsh-fourier-analysis-on-the-uniform-cube-and-t/index.html#khc-infl-eq-fourier-weight).

## Total influence as Fourier weight

The total influence of a Boolean function is `∑_S 4 |S| f̂(S)²`.

Formalized by `StatMech.Probability.khc_totalInfl_eq_fourierWeight`, a theorem declared in [CSLibExt/Complexity/BooleanFunctions/KKL/KKLfromHC.lean, line 621](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Complexity/BooleanFunctions/KKL/KKLfromHC.lean#L621). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/walsh-fourier-analysis-on-the-uniform-cube-and-t/index.html#khc-total-infl-eq-fourier-weight).

## Fourier-form KKL inequality given the hypercontractive bound

The KKL inequality at `p = 1/2` in Fourier form, with the hypercontractive bound as a
 hypothesis: for every Boolean `φ`, if `∑_S ρ^{2|S|} f̂(S)² ≤ ‖f‖²_{1+ρ²}` for all `ρ ∈ [0, 1]`,
 then `c · ∑_{S ≠ ∅} f̂(S)² · log (1 / maxₑ Infₑ(f)) ≤ ∑_S 4 |S| f̂(S)²`, where `f = 1_φ`. The
 hypothesis always holds (`khc_lowDegreeWeight_le`).

Formalized by `StatMech.Probability.khc_LogSobolevStep`, a definition declared in [CSLibExt/Complexity/BooleanFunctions/KKL/KKLfromHC.lean, line 641](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Complexity/BooleanFunctions/KKL/KKLfromHC.lean#L641). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/walsh-fourier-analysis-on-the-uniform-cube-and-t/index.html#khc-log-sobolev-step).

## Hypercontractive form of KKL with constant 0 holds trivially

`khc_LogSobolevStep 0` holds trivially.

Formalized by `StatMech.Probability.khc_logSobolevStep_zero`, a theorem declared in [CSLibExt/Complexity/BooleanFunctions/KKL/KKLfromHC.lean, line 655](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Complexity/BooleanFunctions/KKL/KKLfromHC.lean#L655). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/walsh-fourier-analysis-on-the-uniform-cube-and-t/index.html#khc-log-sobolev-step-zero).

## Hypercontractive form of KKL implies the KKL inequality at $p = 1/2$

The Fourier form `khc_LogSobolevStep c` implies the KKL inequality `KKLHypercontractive (1/2)
 c`.

Formalized by `StatMech.Probability.khc_KKL`, a theorem declared in [CSLibExt/Complexity/BooleanFunctions/KKL/KKLfromHC.lean, line 664](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Complexity/BooleanFunctions/KKL/KKLfromHC.lean#L664). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/walsh-fourier-analysis-on-the-uniform-cube-and-t/index.html#khc-kkl).

## Uniform variance agrees with the canonical Boolean variance

On `Fin n`, the variance under the uniform product weight is `BooleanCube.boolVariance`.

Formalized by `StatMech.Probability.khc_var_half_eq_boolVariance`, a theorem declared in [CSLibExt/Complexity/BooleanFunctions/KKL/KKLfromHC.lean, line 680](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Complexity/BooleanFunctions/KKL/KKLfromHC.lean#L680). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/walsh-fourier-analysis-on-the-uniform-cube-and-t/index.html#khc-var-half-eq-bool-variance).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Walsh–Fourier analysis on the uniform cube and the KKL reduction](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/walsh-fourier-analysis-on-the-uniform-cube-and-t/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/walsh-fourier-analysis-on-the-uniform-cube-and-t)
