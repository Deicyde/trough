---
declaration: section
origin: cited
lean: MathlibExt.Biology.PopulationGenetics.Diffusion.ChainLimit.cauchySeq_apply_of_dense, MathlibExt.Biology.PopulationGenetics.Diffusion.ChainLimit.tendsto_apply_of_dense, MathlibExt.Biology.PopulationGenetics.Diffusion.ChainLimit.dense_polynomialFunctions, MathlibExt.Biology.PopulationGenetics.Diffusion.ChainLimit.floor_mul_eq_zero, ContinuousLinearMap.pow_apply_one, ContinuousLinearMap.pow_nonneg, MathlibExt.Biology.PopulationGenetics.Diffusion.WrightFisherSemigroup.wfStep, MathlibExt.Biology.PopulationGenetics.Diffusion.WrightFisherSemigroup.wfStep_apply
statement: formalized
proof: formalized
---

# Wright–Fisher semigroup and moment duality

52 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/wright-fisher-semigroup-and-moment-duality/index.html).

## Cauchy property of uniform contractions extends from a dense set

Uniformly contractive operators that are Cauchy on a dense set are Cauchy everywhere.

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.ChainLimit.cauchySeq_apply_of_dense`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/ChainLimit.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/Diffusion/ChainLimit.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/wright-fisher-semigroup-and-moment-duality/index.html#cauchy-seq-apply-of-dense).

## Limits of uniform contractions extend from a dense set

Limits of uniformly contractive operators extend from a dense set to the whole space.

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.ChainLimit.tendsto_apply_of_dense`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/ChainLimit.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/Diffusion/ChainLimit.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/wright-fisher-semigroup-and-moment-duality/index.html#tendsto-apply-of-dense).

## Weierstrass approximation theorem on the unit interval

Weierstrass approximation: polynomial functions are dense in `C([0, 1], ℝ)`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.ChainLimit.dense_polynomialFunctions`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/ChainLimit.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/Diffusion/ChainLimit.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/wright-fisher-semigroup-and-moment-duality/index.html#dense-polynomial-functions).

## Natural floor of a nonpositive multiple is zero

If `t ≤ 0`, then the natural floor of `t * M` is zero.

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.ChainLimit.floor_mul_eq_zero`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/ChainLimit.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/Diffusion/ChainLimit.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/wright-fisher-semigroup-and-moment-duality/index.html#floor-mul-eq-zero).

## Powers of a unital endomorphism fix the constant function

Every power of a continuous linear endomorphism fixing `1` also fixes `1`.

Formalized by `ContinuousLinearMap.pow_apply_one`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/ChainLimit.lean, line 94](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/Diffusion/ChainLimit.lean#L94). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/wright-fisher-semigroup-and-moment-duality/index.html#pow-apply-one).

## Powers of a positive endomorphism are positive

Every power of a positive continuous linear endomorphism is positive.

Formalized by `ContinuousLinearMap.pow_nonneg`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/ChainLimit.lean, line 102](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/Diffusion/ChainLimit.lean#L102). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/wright-fisher-semigroup-and-moment-duality/index.html#pow-nonneg).

## One generation of the neutral Wright–Fisher chain

One generation of the neutral Wright–Fisher chain with `M` gene copies, acting on continuous
functions of the allele frequency: `(wfStep M f)(x) = ∑_k f(k/M) C(M, k) x^k (1 - x)^(M - k)`,
which for `M ≥ 1` is the expected value of `f` at the next frequency `Bin(M, x) / M` (the `M`-th
Bernstein operator, Mathlib's `bernsteinApproximation`; the expectation is
`ProbabilityTheory.integral_binomial`). It is a linear
contraction. At `M = 0` it returns the constant `f 0` (Lean's `k / 0 = 0`; no population).

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.WrightFisherSemigroup.wfStep`, a definition declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/Semigroup.lean, line 105](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/Diffusion/Semigroup.lean#L105). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/wright-fisher-semigroup-and-moment-duality/index.html#wf-step).

## Wright–Fisher step is the Bernstein operator

`wfStep M` is the Bernstein approximation operator.

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.WrightFisherSemigroup.wfStep_apply`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/Semigroup.lean, line 125](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/Diffusion/Semigroup.lean#L125). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/wright-fisher-semigroup-and-moment-duality/index.html#wf-step-apply).

## One Wright–Fisher generation is a sup-norm contraction

One Wright–Fisher generation is a contraction for the sup norm.

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.WrightFisherSemigroup.norm_wfStep_le`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/Semigroup.lean, line 128](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/Diffusion/Semigroup.lean#L128). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/wright-fisher-semigroup-and-moment-duality/index.html#norm-wf-step-le).

## One Wright–Fisher generation fixes constants

One Wright–Fisher generation fixes the constant function `1`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.WrightFisherSemigroup.wfStep_apply_one`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/Semigroup.lean, line 132](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/Diffusion/Semigroup.lean#L132). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/wright-fisher-semigroup-and-moment-duality/index.html#wf-step-apply-one).

## One Wright–Fisher generation preserves nonnegativity

One Wright–Fisher generation maps nonnegative functions to nonnegative functions.

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.WrightFisherSemigroup.wfStep_nonneg`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/Semigroup.lean, line 137](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/Diffusion/Semigroup.lean#L137). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/wright-fisher-semigroup-and-moment-duality/index.html#wf-step-nonneg).

## Iterated Wright–Fisher generations are sup-norm contractions

Any number of Wright–Fisher generations is a contraction for the sup norm.

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.WrightFisherSemigroup.norm_wfStep_pow_le`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/Semigroup.lean, line 144](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/Diffusion/Semigroup.lean#L144). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/wright-fisher-semigroup-and-moment-duality/index.html#norm-wf-step-pow-le).

## Moment duality, one generation (polynomial identity)

For `M ≥ 1` gene copies,
`∑_i C(M, i) x^i (1 - x)^(M - i) (i/M)^n = ∑_k S(n, k) M_(k) / M^n · x^k`: the `n`-th moment of
the frequency after one generation equals the generating function of the number of distinct
parents of `n` sampled genes. Holds for every real `x`.

## Sources

- Ethier & Griffiths (1993); Durrett (2008), §7.

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.WrightFisherSemigroup.sum_binomial_mul_div_pow`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/Semigroup.lean, line 224](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/Diffusion/Semigroup.lean#L224). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/wright-fisher-semigroup-and-moment-duality/index.html#sum-binomial-mul-div-pow).

## Moment duality, one generation

If the allele count after one neutral Wright–Fisher
generation with `M ≥ 1` gene copies is `Bin(M, x)`, then
`E_x[(X₁)^n] = ∑_k wfLineageProb M n k · x^k`, where `X₁` is the new frequency and
`wfLineageProb M n k` is the probability that `n` genes have `k` distinct parents.

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.WrightFisherSemigroup.integral_binomial_div_pow`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/Semigroup.lean, line 275](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/Diffusion/Semigroup.lean#L275). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/wright-fisher-semigroup-and-moment-duality/index.html#integral-binomial-div-pow).

## One Wright–Fisher generation acting on monomials

One generation maps `x ^ n` to `∑_k wfLineageProb M n k x ^ k`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.WrightFisherSemigroup.wfStep_X_pow`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/Semigroup.lean, line 283](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/Diffusion/Semigroup.lean#L283). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/wright-fisher-semigroup-and-moment-duality/index.html#wf-step-x-pow).

## Moment duality, `m` generations

For `M ≥ 1` and `n ≤ N`, `m` generations of the
Wright–Fisher chain map `x ^ n` to `∑_k ((wfLineageMatrix N M)^m) n k · x^k`: the `n`-th moment
of the frequency after `m` generations is the generating function of the number of ancestors,
`m` generations back, of `n` sampled genes.

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.WrightFisherSemigroup.wfStep_pow_X_pow`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/Semigroup.lean, line 310](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/Diffusion/Semigroup.lean#L310). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/wright-fisher-semigroup-and-moment-duality/index.html#wf-step-pow-x-pow).

## Dual moment polynomial of Kingman's coalescent

The dual moment polynomial `∑_k P_t(n → k) X^k`, where for `t ≥ 0`,
`P_t(n → k) = exp (t • G) n k` is the probability that `n` lineages of Kingman's coalescent have
`k` ancestors time `t` earlier (time in units of `M = 2N` generations); evaluated at `x` it is
`E_n[x^{A_t}]` for the block-counting process `A`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.WrightFisherSemigroup.dualMomentPoly`, a definition declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/Semigroup.lean, line 344](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/Diffusion/Semigroup.lean#L344). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/wright-fisher-semigroup-and-moment-duality/index.html#dual-moment-poly).

## Wright–Fisher semigroup on polynomials by moment duality

The neutral Wright–Fisher diffusion semigroup on polynomials, defined by moment duality on
the monomial basis: `polySemigroup t (X ^ n) = dualMomentPoly t n`. It is meaningful for
`t ≥ 0`; the formula is defined, and the group law holds, for every real `t`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.WrightFisherSemigroup.polySemigroup`, a definition declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/Semigroup.lean, line 351](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/Diffusion/Semigroup.lean#L351). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/wright-fisher-semigroup-and-moment-duality/index.html#poly-semigroup).

## Dual semigroup on a monomial

The dual semigroup on a monomial is the dual moment polynomial.

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.WrightFisherSemigroup.polySemigroup_X_pow`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/Semigroup.lean, line 355](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/Diffusion/Semigroup.lean#L355). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/wright-fisher-semigroup-and-moment-duality/index.html#poly-semigroup-x-pow).

## Dual semigroup at time zero is the identity

At time `0` the dual semigroup is the identity.

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.WrightFisherSemigroup.polySemigroup_zero`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/Semigroup.lean, line 388](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/Diffusion/Semigroup.lean#L388). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/wright-fisher-semigroup-and-moment-duality/index.html#poly-semigroup-zero).

## Semigroup law

**Semigroup law** on polynomials, from `exp ((s + t) • G) = exp (t • G) * exp (s • G)` and
truncation consistency; holds for all real `s`, `t`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.WrightFisherSemigroup.polySemigroup_add`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/Semigroup.lean, line 400](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/Diffusion/Semigroup.lean#L400). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/wright-fisher-semigroup-and-moment-duality/index.html#poly-semigroup-add).

## Dual semigroup fixes the constant polynomial one

The dual semigroup fixes the constant polynomial `1` (zero lineages stay zero).

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.WrightFisherSemigroup.polySemigroup_one`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/Semigroup.lean, line 414](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/Diffusion/Semigroup.lean#L414). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/wright-fisher-semigroup-and-moment-duality/index.html#poly-semigroup-one).

## Convergence on polynomials

For `t ≥ 0` and every polynomial `p`, `⌊tM⌋` generations
of the Wright–Fisher chain with `M` gene copies applied to `p` converge uniformly on `[0, 1]` to
`polySemigroup t p` as `M → ∞` (moment duality plus Kingman's theorem for the lineage count).

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.WrightFisherSemigroup.tendsto_wfStep_pow_floor_toContinuousMapOn`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/Semigroup.lean, line 441](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/Diffusion/Semigroup.lean#L441). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/wright-fisher-semigroup-and-moment-duality/index.html#tendsto-wf-step-pow-floor-to-continuous).

## Rescaled Wright–Fisher iterates form a Cauchy sequence

For every continuous `f`, the sequence `(wfStep M)^⌊tM⌋ f` is Cauchy in `C([0, 1], ℝ)`: it
converges on the dense set of polynomials and the operators are contractions.

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.WrightFisherSemigroup.cauchySeq_wfStep_pow_floor`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/Semigroup.lean, line 488](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/Diffusion/Semigroup.lean#L488). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/wright-fisher-semigroup-and-moment-duality/index.html#cauchy-seq-wf-step-pow-floor).

## Neutral Wright–Fisher diffusion semigroup

The neutral Wright–Fisher diffusion semigroup on `C([0, 1], ℝ)`, time in units of `M = 2N`
generations: `wfSemigroup t f` is the uniform limit of `(wfStep M)^⌊tM⌋ f` as `M → ∞`
(`tendsto_wfStep_pow_floor`). For `t < 0` it is the identity (a junk value: `⌊tM⌋₊ = 0`).

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.WrightFisherSemigroup.wfSemigroup`, a definition declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/Semigroup.lean, line 502](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/Diffusion/Semigroup.lean#L502). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/wright-fisher-semigroup-and-moment-duality/index.html#wf-semigroup).

## Diffusion approximation of the transition operators (Trotter–Kato, concrete form)

For
every continuous `f`, `⌊tM⌋` generations of the neutral Wright–Fisher chain with `M` gene copies
applied to `f` converge uniformly on `[0, 1]` to `wfSemigroup t f`.

## Sources

- Ethier & Kurtz (1986), ch. 1, §6 (approximation theorems), and ch. 10.

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.WrightFisherSemigroup.tendsto_wfStep_pow_floor`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/Semigroup.lean, line 524](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/Diffusion/Semigroup.lean#L524). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/wright-fisher-semigroup-and-moment-duality/index.html#tendsto-wf-step-pow-floor).

## Contraction

`sup_{[0,1]} |wfSemigroup t f| ≤ sup_{[0,1]} |f|`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.WrightFisherSemigroup.norm_wfSemigroup_le`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/Semigroup.lean, line 529](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/Diffusion/Semigroup.lean#L529). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/wright-fisher-semigroup-and-moment-duality/index.html#norm-wf-semigroup-le).

## Diffusion semigroup agrees with the dual semigroup on polynomials

On polynomials the diffusion semigroup is the dual semigroup, for `t ≥ 0`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.WrightFisherSemigroup.wfSemigroup_toContinuousMapOn`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/Semigroup.lean, line 533](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/Diffusion/Semigroup.lean#L533). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/wright-fisher-semigroup-and-moment-duality/index.html#wf-semigroup-to-continuous-map-on).

## Wright–Fisher semigroup at nonpositive times is the identity

For `t ≤ 0`, `wfSemigroup t` is the identity (at `t = 0` by definition of a semigroup; for
`t < 0` this is a junk value of the definition).

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.WrightFisherSemigroup.wfSemigroup_of_nonpos`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/Semigroup.lean, line 540](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/Diffusion/Semigroup.lean#L540). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/wright-fisher-semigroup-and-moment-duality/index.html#wf-semigroup-of-nonpos).

## Wright–Fisher diffusion semigroup at time zero is the identity

At time `0` the diffusion semigroup is the identity.

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.WrightFisherSemigroup.wfSemigroup_zero`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/Semigroup.lean, line 547](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/Diffusion/Semigroup.lean#L547). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/wright-fisher-semigroup-and-moment-duality/index.html#wf-semigroup-zero).

## Moment duality for the diffusion

**Moment duality for the diffusion** (Ethier & Griffiths 1993). For `t ≥ 0`, the semigroup
applied to `x ↦ x ^ n` is `∑_k P_t(n → k) x^k`, with `P_t = exp (t • G)` the transition matrix of
Kingman's block-counting process `A`; in process language `E_x[(X_t)^n] = E_n[x^{A_t}]` (the
processes themselves are not constructed here).

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.WrightFisherSemigroup.wfSemigroup_X_pow`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/Semigroup.lean, line 554](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/Diffusion/Semigroup.lean#L554). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/wright-fisher-semigroup-and-moment-duality/index.html#wf-semigroup-x-pow).

## Semigroup law

**Semigroup law** for `s, t ≥ 0`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.WrightFisherSemigroup.wfSemigroup_add`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/Semigroup.lean, line 562](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/Diffusion/Semigroup.lean#L562). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/wright-fisher-semigroup-and-moment-duality/index.html#wf-semigroup-add).

## Wright–Fisher diffusion semigroup fixes constants

The diffusion semigroup fixes constants (it is Markov: total mass `1`).

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.WrightFisherSemigroup.wfSemigroup_apply_one`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/Semigroup.lean, line 576](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/Diffusion/Semigroup.lean#L576). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/wright-fisher-semigroup-and-moment-duality/index.html#wf-semigroup-apply-one).

## Positivity

The diffusion semigroup maps nonnegative functions to nonnegative functions.

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.WrightFisherSemigroup.wfSemigroup_nonneg`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/Semigroup.lean, line 586](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/Diffusion/Semigroup.lean#L586). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/wright-fisher-semigroup-and-moment-duality/index.html#wf-semigroup-nonneg).

## Strong continuity

`wfSemigroup t f → f` uniformly as `t → 0⁺`, for every continuous
`f`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.WrightFisherSemigroup.tendsto_wfSemigroup_nhdsGE_zero`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/Semigroup.lean, line 646](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/Diffusion/Semigroup.lean#L646). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/wright-fisher-semigroup-and-moment-duality/index.html#tendsto-wf-semigroup-nhds-ge-zero).

## Neutral Wright–Fisher generator on polynomials

The neutral Wright–Fisher generator on polynomials, `x (1 - x) / 2 · p''`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.WrightFisherSemigroup.polyGenerator`, a definition declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/Semigroup.lean, line 661](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/Diffusion/Semigroup.lean#L661). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/wright-fisher-semigroup-and-moment-duality/index.html#poly-generator).

## Polynomial generator agrees with the neutral Wright–Fisher generator

`polyGenerator` is the neutral Wright–Fisher generator `generator 0` evaluated on `p`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.WrightFisherSemigroup.eval_polyGenerator`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/Semigroup.lean, line 665](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/Diffusion/Semigroup.lean#L665). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/wright-fisher-semigroup-and-moment-duality/index.html#eval-poly-generator).

## Generator on polynomials

For every polynomial `p`,
`(wfSemigroup t p - p) / t → x (1 - x) / 2 · p''` uniformly on `[0, 1]` as `t → 0⁺`.

## Sources

- Ethier & Kurtz (1986), ch. 10; Durrett (2008), §7.

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.WrightFisherSemigroup.tendsto_wfSemigroup_sub_div`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/Semigroup.lean, line 752](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/Diffusion/Semigroup.lean#L752). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/wright-fisher-semigroup-and-moment-duality/index.html#tendsto-wf-semigroup-sub-div).

## Polynomial semigroup dynamics

At every positive time, differentiating the existing
Wright–Fisher semigroup on a polynomial equals applying the semigroup to its generator.

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.WrightFisherSemigroup.hasDerivAt_wfSemigroup_toContinuousMapOn`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/SemigroupMoments.lean, line 117](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/Diffusion/SemigroupMoments.lean#L117). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/wright-fisher-semigroup-and-moment-duality/index.html#has-deriv-at-wf-semigroup-to-continuous).

## Second-moment bound for the Wright–Fisher semigroup

The centered second moment grows at most linearly: `T_t[(y-x)²]&#40;x) ≤ t/4`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.WrightFisherSemigroup.wfSemigroup_second_increment_le`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/SemigroupMoments.lean, line 217](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/Diffusion/SemigroupMoments.lean#L217). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/wright-fisher-semigroup-and-moment-duality/index.html#wf-semigroup-second-increment-le).

## Fourth-moment Kolmogorov bound for the Wright–Fisher semigroup

The fourth centered increment of the neutral Wright–Fisher semigroup satisfies the uniform
Kolmogorov bound `T_t[(y-x)⁴]&#40;x) ≤ (3/16)t²`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.WrightFisherSemigroup.wfSemigroup_fourth_increment_le`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/SemigroupMoments.lean, line 287](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/Diffusion/SemigroupMoments.lean#L287). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/wright-fisher-semigroup-and-moment-duality/index.html#wf-semigroup-fourth-increment-le).

## Wright–Fisher semigroup as a positive operator

The Wright–Fisher semigroup bundled as a positive continuous linear operator.

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.WrightFisherSemigroup.wfSemigroupPositive`, a definition declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/TransitionKernel.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/Diffusion/TransitionKernel.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/wright-fisher-semigroup-and-moment-duality/index.html#wf-semigroup-positive).

## Action of the positive Wright–Fisher operator

Bundling the operator as positive leaves its action on continuous functions unchanged.

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.WrightFisherSemigroup.wfSemigroupPositive_apply`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/TransitionKernel.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/Diffusion/TransitionKernel.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/wright-fisher-semigroup-and-moment-duality/index.html#wf-semigroup-positive-apply).

## Positive Wright–Fisher operator fixes constants

The positive Wright–Fisher operator fixes the constant function `1`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.WrightFisherSemigroup.wfSemigroupPositive_apply_one`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/TransitionKernel.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/Diffusion/TransitionKernel.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/wright-fisher-semigroup-and-moment-duality/index.html#wf-semigroup-positive-apply-one).

## Semigroup law for the positive Wright–Fisher operator

The positive-operator form of the Wright–Fisher semigroup law.

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.WrightFisherSemigroup.wfSemigroupPositive_add`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/TransitionKernel.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/Diffusion/TransitionKernel.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/wright-fisher-semigroup-and-moment-duality/index.html#wf-semigroup-positive-add).

## Transition kernel of the neutral Wright–Fisher diffusion

The transition kernel of the neutral Wright–Fisher diffusion at time `t`. For nonnegative `t`
it is the probabilistic transition corresponding to `wfSemigroup t`; for negative `t`, both the
operator and kernel are the identity junk value inherited from `wfSemigroup`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.WrightFisherSemigroup.wfTransitionKernel`, a definition declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/TransitionKernel.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/Diffusion/TransitionKernel.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/wright-fisher-semigroup-and-moment-duality/index.html#wf-transition-kernel).

## Wright–Fisher transition kernel represents the semigroup

Integration against the transition kernel agrees with the Wright–Fisher semigroup on every
continuous test function and every initial allele frequency.

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.WrightFisherSemigroup.integral_wfTransitionKernel`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/TransitionKernel.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/Diffusion/TransitionKernel.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/wright-fisher-semigroup-and-moment-duality/index.html#integral-wf-transition-kernel).

## Wright–Fisher transition kernel is the identity at nonpositive times

For nonpositive times, the Wright–Fisher transition is the identity kernel.

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.WrightFisherSemigroup.wfTransitionKernel_of_nonpos`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/TransitionKernel.lean, line 90](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/Diffusion/TransitionKernel.lean#L90). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/wright-fisher-semigroup-and-moment-duality/index.html#wf-transition-kernel-of-nonpos).

## Wright–Fisher transition kernel is the identity at time zero

At time zero the Wright–Fisher transition is the identity kernel.

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.WrightFisherSemigroup.wfTransitionKernel_zero`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/TransitionKernel.lean, line 99](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/Diffusion/TransitionKernel.lean#L99). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/wright-fisher-semigroup-and-moment-duality/index.html#wf-transition-kernel-zero).

## Wright–Fisher transitions at time zero are Dirac masses

Pointwise identity law for the transition kernel at time zero.

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.WrightFisherSemigroup.wfTransitionKernel_zero_apply`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/TransitionKernel.lean, line 104](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/Diffusion/TransitionKernel.lean#L104). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/wright-fisher-semigroup-and-moment-duality/index.html#wf-transition-kernel-zero-apply).

## Chapman–Kolmogorov equation for the Wright–Fisher diffusion

Chapman–Kolmogorov law for the Wright–Fisher transition kernels. With Mathlib's convention,
`K_t ∘ₖ K_s` first evolves for time `s` and then for time `t`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.WrightFisherSemigroup.wfTransitionKernel_add`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/TransitionKernel.lean, line 109](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/Diffusion/TransitionKernel.lean#L109). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/wright-fisher-semigroup-and-moment-duality/index.html#wf-transition-kernel-add).

## Kernel form of Wright–Fisher moment duality

Kernel form of Wright–Fisher moment duality: transition-kernel moments are the transition
probabilities of Kingman's block-counting process.

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.WrightFisherSemigroup.integral_wfTransitionKernel_X_pow`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/TransitionKernel.lean, line 117](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/Diffusion/TransitionKernel.lean#L117). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/wright-fisher-semigroup-and-moment-duality/index.html#integral-wf-transition-kernel-x-pow).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Wright–Fisher semigroup and moment duality](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/wright-fisher-semigroup-and-moment-duality/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Biology/population-genetics/diffusion-theory/wright-fisher-semigroup-and-moment-duality)
