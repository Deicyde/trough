---
declaration: section
origin: cited
lean: MathlibExt.Dynamics.Ergodic.KingmanWanted.kingman_subadditive, StatMech.Kingman.integral_comp_measurePreserving, StatMech.Kingman.integral_comp_iterate, StatMech.Kingman.SubadditiveCocycle, StatMech.Kingman.SubadditiveCocycle.expSeq, StatMech.Kingman.SubadditiveCocycle.expSeq_subadditive, StatMech.Kingman.SubadditiveCocycle.subadditive_expSeq, StatMech.Kingman.SubadditiveCocycle.ae_le_birkhoffSum
statement: formalized
proof: formalized
---

# Kingman's subadditive ergodic theorem

49 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/ergodic-theory/kingman-s-subadditive-ergodic-theorem/index.html).

## Kingman's subadditive ergodic theorem (nonnegative case)

Let $\mu$ be a probability measure
on a measurable space $\alpha$ and let $T : \alpha \to \alpha$ preserve $\mu$. Let
$(f_n)_{n \in \mathbb{N}}$ be functions $\alpha \to \mathbb{R}$, each measurable and
$\mu$-integrable, such that for every $n$ the inequality $f_n \ge 0$ holds $\mu$-almost
everywhere, $f_0 = 0$ holds $\mu$-almost everywhere, and for all natural numbers $m$ and $n$ the
inequality $f_{m+n}(x) \le f_m(x) + f_n(T^m x)$ holds for $\mu$-almost every $x$. Then there is a
$\mu$-integrable function $g : \alpha \to \mathbb{R}$ such that $g(T x) = g(x)$ for $\mu$-almost
every $x$ and $f_n(x)/n$ converges to $g(x)$ as $n \to \infty$ for $\mu$-almost every $x$.

## Sources

- J. F. C. Kingman, "The Ergodic Theory of Subadditive Stochastic Processes", Journal of the Royal Statistical Society Series B 30 (1968), 499–510, DOI 10.1111/j.2517-6161.1968.tb00749.x.

Formalized by `MathlibExt.Dynamics.Ergodic.KingmanWanted.kingman_subadditive`, a theorem declared in [MathlibExt/Dynamics/Ergodic/Kingman.lean, line 1131](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Dynamics/Ergodic/Kingman.lean#L1131). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/ergodic-theory/kingman-s-subadditive-ergodic-theorem/index.html#kingman-subadditive).

## Integral is invariant under a measure-preserving map

The integral is invariant under a measure-preserving map: `∫ g ∘ T dμ = ∫ g dμ` for
a.e.-strongly measurable `g`.

Formalized by `StatMech.Kingman.integral_comp_measurePreserving`, a theorem declared in [MathlibExt/Dynamics/Ergodic/KingmanSigned/Basic.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Dynamics/Ergodic/KingmanSigned/Basic.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/ergodic-theory/kingman-s-subadditive-ergodic-theorem/index.html#integral-comp-measure-preserving).

## Integral is invariant under iterates of a measure-preserving map

The integral is invariant under iterates of a measure-preserving map:
`∫ g ∘ T^[m] dμ = ∫ g dμ` for a.e.-strongly measurable `g`. See also
`MathlibExt.Probability.BirkhoffErgodicL1.integral_comp_iterate_of_measurePreserving`, which
assumes `g` integrable.

Formalized by `StatMech.Kingman.integral_comp_iterate`, a theorem declared in [MathlibExt/Dynamics/Ergodic/KingmanSigned/Basic.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Dynamics/Ergodic/KingmanSigned/Basic.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/ergodic-theory/kingman-s-subadditive-ergodic-theorem/index.html#integral-comp-iterate).

## Subadditive cocycle over a measure-preserving map

`X` is a subadditive cocycle over `T`: `T` preserves `μ`, every `X n` is integrable, and
`X (m + n) ≤ X m + X n ∘ T^[m]` almost everywhere.

Formalized by `StatMech.Kingman.SubadditiveCocycle`, a structure declared in [MathlibExt/Dynamics/Ergodic/KingmanSigned/Basic.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Dynamics/Ergodic/KingmanSigned/Basic.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/ergodic-theory/kingman-s-subadditive-ergodic-theorem/index.html#subadditive-cocycle).

## Expectation sequence of a cocycle

The expectation `∫ X n dμ` of the `n`-th term.

Formalized by `StatMech.Kingman.SubadditiveCocycle.expSeq`, a definition declared in [MathlibExt/Dynamics/Ergodic/KingmanSigned/Basic.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Dynamics/Ergodic/KingmanSigned/Basic.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/ergodic-theory/kingman-s-subadditive-ergodic-theorem/index.html#exp-seq).

## Expectations of a subadditive cocycle are subadditive

The expectations of a subadditive cocycle are subadditive.

Formalized by `StatMech.Kingman.SubadditiveCocycle.expSeq_subadditive`, a theorem declared in [MathlibExt/Dynamics/Ergodic/KingmanSigned/Basic.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Dynamics/Ergodic/KingmanSigned/Basic.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/ergodic-theory/kingman-s-subadditive-ergodic-theorem/index.html#exp-seq-subadditive).

## Expectations of a subadditive cocycle form a subadditive sequence

The expectations of a subadditive cocycle form a `Subadditive` sequence.

Formalized by `StatMech.Kingman.SubadditiveCocycle.subadditive_expSeq`, a theorem declared in [MathlibExt/Dynamics/Ergodic/KingmanSigned/Basic.lean, line 104](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Dynamics/Ergodic/KingmanSigned/Basic.lean#L104). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/ergodic-theory/kingman-s-subadditive-ergodic-theorem/index.html#subadditive-exp-seq).

## Subadditive cocycle bounded by Birkhoff sums of its first term

Iterating subadditivity: `X n ≤ ∑_{k<n} X 1 ∘ T^[k]` almost everywhere, for all `n ≥ 1`.

Formalized by `StatMech.Kingman.SubadditiveCocycle.ae_le_birkhoffSum`, a theorem declared in [MathlibExt/Dynamics/Ergodic/KingmanSigned/Basic.lean, line 108](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Dynamics/Ergodic/KingmanSigned/Basic.lean#L108). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/ergodic-theory/kingman-s-subadditive-ergodic-theorem/index.html#ae-le-birkhoff-sum).

## Expectation of a subadditive cocycle grows at most linearly

`∫ X n dμ ≤ n ∫ X 1 dμ` for `n ≥ 1`.

Formalized by `StatMech.Kingman.SubadditiveCocycle.expSeq_le_nsmul`, a theorem declared in [MathlibExt/Dynamics/Ergodic/KingmanSigned/Basic.lean, line 126](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Dynamics/Ergodic/KingmanSigned/Basic.lean#L126). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/ergodic-theory/kingman-s-subadditive-ergodic-theorem/index.html#exp-seq-le-nsmul).

## Time constant of a subadditive cocycle

The time constant `lim_n (∫ X n dμ) / n = inf_n (∫ X n dμ) / n` (Fekete's lemma); it is
meaningful when `expSeq n / n` is bounded below.

Formalized by `StatMech.Kingman.SubadditiveCocycle.gamma`, a definition declared in [MathlibExt/Dynamics/Ergodic/KingmanSigned/Basic.lean, line 148](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Dynamics/Ergodic/KingmanSigned/Basic.lean#L148). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/ergodic-theory/kingman-s-subadditive-ergodic-theorem/index.html#gamma).

## Fekete's lemma for the expectations of a subadditive cocycle

Fekete's lemma for the expectations: `expSeq n / n → gamma` when bounded below.

Formalized by `StatMech.Kingman.SubadditiveCocycle.tendsto_expSeq_div`, a theorem declared in [MathlibExt/Dynamics/Ergodic/KingmanSigned/Basic.lean, line 152](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Dynamics/Ergodic/KingmanSigned/Basic.lean#L152). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/ergodic-theory/kingman-s-subadditive-ergodic-theorem/index.html#tendsto-exp-seq-div).

## Time constant is a lower bound for normalized expectations

`gamma ≤ expSeq n / n` for every `n ≠ 0`.

Formalized by `StatMech.Kingman.SubadditiveCocycle.gamma_le_div`, a theorem declared in [MathlibExt/Dynamics/Ergodic/KingmanSigned/Basic.lean, line 158](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Dynamics/Ergodic/KingmanSigned/Basic.lean#L158). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/ergodic-theory/kingman-s-subadditive-ergodic-theorem/index.html#gamma-le-div).

## Time constant is at most the first expectation

`gamma ≤ ∫ X 1 dμ`.

Formalized by `StatMech.Kingman.SubadditiveCocycle.gamma_le_expSeq_one`, a theorem declared in [MathlibExt/Dynamics/Ergodic/KingmanSigned/Basic.lean, line 164](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Dynamics/Ergodic/KingmanSigned/Basic.lean#L164). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/ergodic-theory/kingman-s-subadditive-ergodic-theorem/index.html#gamma-le-exp-seq-one).

## Normalized expectations of a nonnegative cocycle are bounded below

For a nonnegative cocycle, `expSeq n / n` is bounded below by `0`.

Formalized by `StatMech.Kingman.SubadditiveCocycle.bddBelow_of_nonneg`, a theorem declared in [MathlibExt/Dynamics/Ergodic/KingmanSigned/Basic.lean, line 171](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Dynamics/Ergodic/KingmanSigned/Basic.lean#L171). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/ergodic-theory/kingman-s-subadditive-ergodic-theorem/index.html#bdd-below-of-nonneg).

## Cocycle inequality holds for all indices almost everywhere

The cocycle inequality holds for all `m, n` simultaneously, almost everywhere.

Formalized by `StatMech.KingmanAE.ae_all_subadditive`, a theorem declared in [MathlibExt/Dynamics/Ergodic/KingmanSigned/AE.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Dynamics/Ergodic/KingmanSigned/AE.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/ergodic-theory/kingman-s-subadditive-ergodic-theorem/index.html#ae-all-subadditive).

## Block decomposition bound for a subadditive cocycle

Block decomposition: `X (q k) ≤ ∑_{j<q} X k ∘ T^{j k}` almost everywhere.

Formalized by `StatMech.KingmanAE.ae_le_block_birkhoffSum`, a theorem declared in [MathlibExt/Dynamics/Ergodic/KingmanSigned/AE.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Dynamics/Ergodic/KingmanSigned/AE.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/ergodic-theory/kingman-s-subadditive-ergodic-theorem/index.html#ae-le-block-birkhoff-sum).

## Integrable function along an orbit divided by time tends to zero

For integrable `g`, `g (T^[m] x) / m → 0` almost everywhere.

Formalized by `StatMech.KingmanAE.tendsto_comp_div_atTop`, a theorem declared in [MathlibExt/Dynamics/Ergodic/KingmanSigned/AE.lean, line 99](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Dynamics/Ergodic/KingmanSigned/AE.lean#L99). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/ergodic-theory/kingman-s-subadditive-ergodic-theorem/index.html#tendsto-comp-div-at-top).

## Dominating function for remainder terms in Kingman's theorem

The integrable dominating function `∑_{r<k} (X r)⁺` for the remainder terms `X r`, `r < k`.

Formalized by `StatMech.KingmanAE.remDom`, a definition declared in [MathlibExt/Dynamics/Ergodic/KingmanSigned/AE.lean, line 179](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Dynamics/Ergodic/KingmanSigned/AE.lean#L179). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/ergodic-theory/kingman-s-subadditive-ergodic-theorem/index.html#rem-dom).

## Upper limit of a cocycle bounded by Birkhoff limits of blocks

For each `k ≥ 1`, `limsup X n / n ≤ birkhoffLimit (T^[k]) (X k) / k` almost everywhere.

Formalized by `StatMech.KingmanAE.gStar_le`, a theorem declared in [MathlibExt/Dynamics/Ergodic/KingmanSigned/AE.lean, line 199](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Dynamics/Ergodic/KingmanSigned/AE.lean#L199). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/ergodic-theory/kingman-s-subadditive-ergodic-theorem/index.html#g-star-le).

## Upper limit of a normalized subadditive cocycle

The upper limit `limsup_n X n x / n` in `EReal`. The map `T` is a parameter only so that
the notation records the cocycle's base map.

Formalized by `StatMech.KingmanAE.gStar`, a definition declared in [MathlibExt/Dynamics/Ergodic/KingmanSigned/AE.lean, line 281](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Dynamics/Ergodic/KingmanSigned/AE.lean#L281). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/ergodic-theory/kingman-s-subadditive-ergodic-theorem/index.html#g-star).

## Lower limit of a normalized subadditive cocycle

The lower limit `liminf_n X n x / n` in `EReal`.

Formalized by `StatMech.KingmanAE.gStarLow`, a definition declared in [MathlibExt/Dynamics/Ergodic/KingmanSigned/AE.lean, line 286](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Dynamics/Ergodic/KingmanSigned/AE.lean#L286). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/ergodic-theory/kingman-s-subadditive-ergodic-theorem/index.html#g-star-low).

## Upper limit of a normalized cocycle is finite almost everywhere

`limsup X n / n < ⊤` almost everywhere.

Formalized by `StatMech.KingmanAE.gStar_lt_top_ae`, a theorem declared in [MathlibExt/Dynamics/Ergodic/KingmanSigned/AE.lean, line 356](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Dynamics/Ergodic/KingmanSigned/AE.lean#L356). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/ergodic-theory/kingman-s-subadditive-ergodic-theorem/index.html#g-star-lt-top-ae).

## Kingman limit of a subadditive cocycle

The limit `lim X n / n` in Kingman's theorem, defined as `limsup X n / n` cast to `ℝ` (so it is
`0` where the `limsup` is infinite).

Formalized by `StatMech.KingmanAE.kingmanLimit`, a definition declared in [MathlibExt/Dynamics/Ergodic/KingmanSigned/AE.lean, line 367](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Dynamics/Ergodic/KingmanSigned/AE.lean#L367). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/ergodic-theory/kingman-s-subadditive-ergodic-theorem/index.html#kingman-limit).

## Almost-everywhere convergence to the Kingman limit

If `g* ≤ g_*` and `g* > ⊥` almost everywhere, then `X n / n → kingmanLimit` almost
everywhere.

Formalized by `StatMech.KingmanAE.tendsto_div_kingmanLimit_ae`, a theorem declared in [MathlibExt/Dynamics/Ergodic/KingmanSigned/AE.lean, line 371](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Dynamics/Ergodic/KingmanSigned/AE.lean#L371). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/ergodic-theory/kingman-s-subadditive-ergodic-theorem/index.html#tendsto-div-kingman-limit-ae).

## Invariance of the Kingman limit

Under the hypotheses of `tendsto_div_kingmanLimit_ae` and integrability of the limit, the
limit is `T`-invariant almost everywhere.

Formalized by `StatMech.KingmanAE.kingmanLimit_comp_ae`, a theorem declared in [MathlibExt/Dynamics/Ergodic/KingmanSigned/AE.lean, line 431](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Dynamics/Ergodic/KingmanSigned/AE.lean#L431). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/ergodic-theory/kingman-s-subadditive-ergodic-theorem/index.html#kingman-limit-comp-ae).

## Integrability of the Kingman limit for nonnegative cocycles

For a nonnegative cocycle, `kingmanLimit` is integrable.

Formalized by `StatMech.KingmanAE.integrable_kingmanLimit`, a theorem declared in [MathlibExt/Dynamics/Ergodic/KingmanSigned/AE.lean, line 493](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Dynamics/Ergodic/KingmanSigned/AE.lean#L493). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/ergodic-theory/kingman-s-subadditive-ergodic-theorem/index.html#integrable-kingman-limit).

## Integral of the Kingman limit is at most the time constant

For a nonnegative cocycle, `∫ kingmanLimit ≤ gamma`.

Formalized by `StatMech.KingmanAE.integral_kingmanLimit_le_gamma`, a theorem declared in [MathlibExt/Dynamics/Ergodic/KingmanSigned/AE.lean, line 524](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Dynamics/Ergodic/KingmanSigned/AE.lean#L524). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/ergodic-theory/kingman-s-subadditive-ergodic-theorem/index.html#integral-kingman-limit-le-gamma).

## Real lower limit of a normalized cocycle

The lower limit `liminf_n X n x / n`, cast to `ℝ`.

Formalized by `StatMech.KingmanFilling.gLow`, a definition declared in [MathlibExt/Dynamics/Ergodic/KingmanSigned/Filling.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Dynamics/Ergodic/KingmanSigned/Filling.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/ergodic-theory/kingman-s-subadditive-ergodic-theorem/index.html#g-low).

## Ordered extended reals with equal real parts are equal

Two extended reals `x ≤ y` with `x ≠ ⊥`, `y ≠ ⊤` and equal real parts are equal.

Formalized by `StatMech.KingmanFilling.eq_of_le_toReal_eq`, a theorem declared in [MathlibExt/Dynamics/Ergodic/KingmanSigned/Filling.lean, line 94](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Dynamics/Ergodic/KingmanSigned/Filling.lean#L94). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/ergodic-theory/kingman-s-subadditive-ergodic-theorem/index.html#eq-of-le-to-real-eq).

## Lower limit of a cocycle is nondecreasing along the map

The lower limit is nondecreasing along `T`: `g_* ≤ g_* ∘ T` almost everywhere.

Formalized by `StatMech.KingmanFilling.gStarLow_le_comp`, a theorem declared in [MathlibExt/Dynamics/Ergodic/KingmanSigned/Filling.lean, line 101](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Dynamics/Ergodic/KingmanSigned/Filling.lean#L101). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/ergodic-theory/kingman-s-subadditive-ergodic-theorem/index.html#g-star-low-le-comp).

## Bad set in the greedy decomposition for Kingman's theorem

The bad set: points where `X m x > (gLow x + ε) m` for every block length `1 ≤ m ≤ N`.

Formalized by `StatMech.KingmanFilling.badSet`, a definition declared in [MathlibExt/Dynamics/Ergodic/KingmanSigned/Filling.lean, line 156](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Dynamics/Ergodic/KingmanSigned/Filling.lean#L156). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/ergodic-theory/kingman-s-subadditive-ergodic-theorem/index.html#bad-set).

## Per-step budget of the greedy decomposition

The per-step budget `gLow + ε + 1_{badSet} X 1` of the greedy decomposition.

Formalized by `StatMech.KingmanFilling.dep`, a definition declared in [MathlibExt/Dynamics/Ergodic/KingmanSigned/Filling.lean, line 160](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Dynamics/Ergodic/KingmanSigned/Filling.lean#L160). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/ergodic-theory/kingman-s-subadditive-ergodic-theorem/index.html#dep).

## Cost of a bad step in the greedy decomposition

The cost `1_{badSet} X 1` of a bad step.

Formalized by `StatMech.KingmanFilling.badCost`, a definition declared in [MathlibExt/Dynamics/Ergodic/KingmanSigned/Filling.lean, line 164](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Dynamics/Ergodic/KingmanSigned/Filling.lean#L164). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/ergodic-theory/kingman-s-subadditive-ergodic-theorem/index.html#bad-cost).

## Greedy decomposition along an orbit

Greedy decomposition along one orbit: `X n (T^[s] x)` is at most the sum of the budgets
`dep` over `n` steps plus one remainder term, for every `n` and starting time `s`.

Formalized by `StatMech.KingmanFilling.greedy`, a theorem declared in [MathlibExt/Dynamics/Ergodic/KingmanSigned/Filling.lean, line 180](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Dynamics/Ergodic/KingmanSigned/Filling.lean#L180). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/ergodic-theory/kingman-s-subadditive-ergodic-theorem/index.html#greedy).

## Windowed greedy bound from time zero

The greedy bound from time `0`, with the remainder bounded by a sum over the last window.

Formalized by `StatMech.KingmanFilling.greedy_windowed`, a theorem declared in [MathlibExt/Dynamics/Ergodic/KingmanSigned/Filling.lean, line 282](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Dynamics/Ergodic/KingmanSigned/Filling.lean#L282). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/ergodic-theory/kingman-s-subadditive-ergodic-theorem/index.html#greedy-windowed).

## Time constant is at most the integral of the lower limit

The time constant is at most `∫ g_*`.

Formalized by `StatMech.KingmanFilling.gamma_le_integral_gLow`, a theorem declared in [MathlibExt/Dynamics/Ergodic/KingmanSigned/Filling.lean, line 544](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Dynamics/Ergodic/KingmanSigned/Filling.lean#L544). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/ergodic-theory/kingman-s-subadditive-ergodic-theorem/index.html#gamma-le-integral-g-low).

## Upper and lower limits of a nonnegative cocycle agree

For a nonnegative cocycle the upper and lower limits of `X n / n` agree almost everywhere.

Formalized by `StatMech.KingmanFilling.gStar_le_gStarLow_ae`, a theorem declared in [MathlibExt/Dynamics/Ergodic/KingmanSigned/Filling.lean, line 586](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Dynamics/Ergodic/KingmanSigned/Filling.lean#L586). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/ergodic-theory/kingman-s-subadditive-ergodic-theorem/index.html#g-star-le-g-star-low-ae).

## Kingman's subadditive ergodic theorem

**Kingman's subadditive ergodic theorem** for nonnegative cocycles: `X n / n` converges almost
everywhere to `kingmanLimit T X` (J. F. C. Kingman, 1968; proof of J. M. Steele, 1989).

Formalized by `StatMech.KingmanFilling.tendsto_div_kingmanLimit_ae_of_nonneg`, a theorem declared in [MathlibExt/Dynamics/Ergodic/KingmanSigned/Filling.lean, line 592](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Dynamics/Ergodic/KingmanSigned/Filling.lean#L592). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/ergodic-theory/kingman-s-subadditive-ergodic-theorem/index.html#tendsto-div-kingman-limit-ae-of-nonneg).

## Additive cocycle of Birkhoff sums of the first term

The additive cocycle `n ↦ ∑_{k<n} X 1 ∘ T^[k]` (the Birkhoff sums of `X 1`).

Formalized by `StatMech.KingmanSigned.addCoc`, a definition declared in [MathlibExt/Dynamics/Ergodic/KingmanSigned.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Dynamics/Ergodic/KingmanSigned.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/ergodic-theory/kingman-s-subadditive-ergodic-theorem/index.html#add-coc).

## Subadditivity defect of a cocycle

The subadditivity defect `addCoc n - X n` (`0` at `n = 0`); it is nonnegative a.e.

Formalized by `StatMech.KingmanSigned.Zc`, a definition declared in [MathlibExt/Dynamics/Ergodic/KingmanSigned.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Dynamics/Ergodic/KingmanSigned.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/ergodic-theory/kingman-s-subadditive-ergodic-theorem/index.html#zc).

## Negative subadditivity defect of a cocycle

The negative defect `X n - addCoc n` (`0` at `n = 0`), a nonpositive subadditive cocycle.

Formalized by `StatMech.KingmanSigned.Wc`, a definition declared in [MathlibExt/Dynamics/Ergodic/KingmanSigned.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Dynamics/Ergodic/KingmanSigned.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/ergodic-theory/kingman-s-subadditive-ergodic-theorem/index.html#wc).

## Negative defect is a subadditive cocycle

The negative defect is a subadditive cocycle.

Formalized by `StatMech.KingmanSigned.Wc_subaddCocycle`, a theorem declared in [MathlibExt/Dynamics/Ergodic/KingmanSigned.lean, line 115](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Dynamics/Ergodic/KingmanSigned.lean#L115). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/ergodic-theory/kingman-s-subadditive-ergodic-theorem/index.html#wc-subadd-cocycle).

## Shifted subadditivity defect of a cocycle

The shifted defect `X n + M n - addCoc n`, a subadditive cocycle for every `M`.

Formalized by `StatMech.KingmanSigned.Sc`, a definition declared in [MathlibExt/Dynamics/Ergodic/KingmanSigned.lean, line 148](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Dynamics/Ergodic/KingmanSigned.lean#L148). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/ergodic-theory/kingman-s-subadditive-ergodic-theorem/index.html#sc).

## Truncated subadditivity defect of a cocycle

The truncated defect `(Sc M n)⁺ = (M n - Zc n)⁺`, a nonnegative subadditive cocycle.

Formalized by `StatMech.KingmanSigned.Vc`, a definition declared in [MathlibExt/Dynamics/Ergodic/KingmanSigned.lean, line 152](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Dynamics/Ergodic/KingmanSigned.lean#L152). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/ergodic-theory/kingman-s-subadditive-ergodic-theorem/index.html#vc).

## Truncated defect is a nonnegative subadditive cocycle

The truncated defect is a nonnegative subadditive cocycle.

Formalized by `StatMech.KingmanSigned.Vc_subaddCocycle`, a theorem declared in [MathlibExt/Dynamics/Ergodic/KingmanSigned.lean, line 174](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Dynamics/Ergodic/KingmanSigned.lean#L174). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/ergodic-theory/kingman-s-subadditive-ergodic-theorem/index.html#vc-subadd-cocycle).

## Lower limit of the normalized defect is finite almost everywhere

If the time constant is finite, `liminf_n Zc n / n < ∞` almost everywhere (Fatou).

Formalized by `StatMech.KingmanSigned.ae_liminf_lt_top`, a theorem declared in [MathlibExt/Dynamics/Ergodic/KingmanSigned.lean, line 230](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Dynamics/Ergodic/KingmanSigned.lean#L230). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/ergodic-theory/kingman-s-subadditive-ergodic-theorem/index.html#ae-liminf-lt-top).

## Kingman's theorem: normalized cocycle converges almost everywhere

If the time constant is finite, `X n / n` converges almost everywhere.

Formalized by `StatMech.KingmanSigned.ae_tendsto_X_div`, a theorem declared in [MathlibExt/Dynamics/Ergodic/KingmanSigned.lean, line 318](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Dynamics/Ergodic/KingmanSigned.lean#L318). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/ergodic-theory/kingman-s-subadditive-ergodic-theorem/index.html#ae-tendsto-x-div).

## Kingman's subadditive ergodic theorem

**Kingman's subadditive ergodic theorem** (J. F. C. Kingman, *The ergodic theory of
subadditive stochastic processes*, 1968): if `X` is a subadditive cocycle over a map `T`
preserving the finite measure `μ` and `inf_n (∫ X n dμ) / n > -∞`, then `X n / n` converges
`μ`-almost everywhere to the finite limit `kingmanLimit T X`. The sign of `X` is arbitrary.
Invariance and integrability of the limit, and `∫ kingmanLimit = gamma`, are not stated here; for
nonnegative cocycles see `exists_invariant_limit_of_nonneg`, which contains
`MathlibExt.Dynamics.Ergodic.KingmanWanted.kingman_subadditive`.

Formalized by `StatMech.KingmanSigned.kingman_ae_general`, a theorem declared in [MathlibExt/Dynamics/Ergodic/KingmanSigned.lean, line 355](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Dynamics/Ergodic/KingmanSigned.lean#L355). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/ergodic-theory/kingman-s-subadditive-ergodic-theorem/index.html#kingman-ae-general).

## Kingman's subadditive ergodic theorem for nonnegative cocycles

Kingman's theorem for nonnegative cocycles, with integrable and invariant limit: if `T`
preserves the finite measure `μ` and `X` is a nonnegative integrable subadditive cocycle, then
`X n / n` converges a.e. to an integrable `T`-invariant function. This is
`MathlibExt.Dynamics.Ergodic.KingmanWanted.kingman_subadditive` without its hypotheses that each
`X n` is measurable and `X 0 = 0`, and for finite rather than probability measures.

Formalized by `StatMech.KingmanSigned.exists_invariant_limit_of_nonneg`, a theorem declared in [MathlibExt/Dynamics/Ergodic/KingmanSigned.lean, line 366](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Dynamics/Ergodic/KingmanSigned.lean#L366). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/ergodic-theory/kingman-s-subadditive-ergodic-theorem/index.html#exists-invariant-limit-of-nonneg).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Kingman's subadditive ergodic theorem](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/ergodic-theory/kingman-s-subadditive-ergodic-theorem/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Dynamics/ergodic-theory/kingman-s-subadditive-ergodic-theorem)
