---
declaration: section
origin: cited
lean: StatMech.dbl, StatMech.boxDoubled, StatMech.card_boxDoubled, StatMech.card_boxFamily_le_boxDoubled, StatMech.upComp, StatMech.downLeft, StatMech.upRight, StatMech.doubleCompress
statement: formalized
proof: formalized
---

# Doubled ground set in Reimer's proof

19 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/reimer-inequality/doubled-ground-set-in-reimer-s-proof/index.html).

## Encoding a pair of finsets in the doubled ground set

The finset `inl '' S ∪ inr '' T` of `α ⊕ α`, encoding the pair `(S, T)`.

Formalized by `StatMech.dbl`, a definition declared in [MathlibExt/Probability/CorrelationInequalities/ReimerDoubled.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/CorrelationInequalities/ReimerDoubled.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/reimer-inequality/doubled-ground-set-in-reimer-s-proof/index.html#dbl).

## Doubled family of disjoint pairs

The family of `dbl S T` over disjoint pairs `S ∈ 𝒜`, `T ∈ ℬ`.

Formalized by `StatMech.boxDoubled`, a definition declared in [MathlibExt/Probability/CorrelationInequalities/ReimerDoubled.lean, line 91](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/CorrelationInequalities/ReimerDoubled.lean#L91). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/reimer-inequality/doubled-ground-set-in-reimer-s-proof/index.html#box-doubled).

## Size of the doubled disjoint-pair family

The size of `boxDoubled 𝒜 ℬ` is the number of disjoint pairs in `𝒜 × ℬ`.

Formalized by `StatMech.card_boxDoubled`, a theorem declared in [MathlibExt/Probability/CorrelationInequalities/ReimerDoubled.lean, line 103](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/CorrelationInequalities/ReimerDoubled.lean#L103). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/reimer-inequality/doubled-ground-set-in-reimer-s-proof/index.html#card-box-doubled).

## Disjoint-union family is no larger than the doubled family

`#(𝒜 ○ ℬ) ≤ #(boxDoubled 𝒜 ℬ)`: distinct disjoint pairs can have the same union.

Formalized by `StatMech.card_boxFamily_le_boxDoubled`, a theorem declared in [MathlibExt/Probability/CorrelationInequalities/ReimerDoubled.lean, line 119](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/CorrelationInequalities/ReimerDoubled.lean#L119). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/reimer-inequality/doubled-ground-set-in-reimer-s-proof/index.html#card-box-family-le-box-doubled).

## Up-compression at a point of the doubled ground set

Up-compression of a family on `α ⊕ α` at the point `a` (`UV.compression {a} ∅`).

Formalized by `StatMech.upComp`, a definition declared in [MathlibExt/Probability/CorrelationInequalities/ReimerDoubled.lean, line 132](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/CorrelationInequalities/ReimerDoubled.lean#L132). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/reimer-inequality/doubled-ground-set-in-reimer-s-proof/index.html#up-comp).

## Down-compression at the left copy of a coordinate

Down-compression at the left copy `inl i`.

Formalized by `StatMech.downLeft`, a definition declared in [MathlibExt/Probability/CorrelationInequalities/ReimerDoubled.lean, line 144](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/CorrelationInequalities/ReimerDoubled.lean#L144). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/reimer-inequality/doubled-ground-set-in-reimer-s-proof/index.html#down-left).

## Up-compression at the right copy of a coordinate

Up-compression at the right copy `inr i`.

Formalized by `StatMech.upRight`, a definition declared in [MathlibExt/Probability/CorrelationInequalities/ReimerDoubled.lean, line 148](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/CorrelationInequalities/ReimerDoubled.lean#L148). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/reimer-inequality/doubled-ground-set-in-reimer-s-proof/index.html#up-right).

## Double compression at a coordinate

Down-compression at `inl i` followed by up-compression at `inr i`.

Formalized by `StatMech.doubleCompress`, a definition declared in [MathlibExt/Probability/CorrelationInequalities/ReimerDoubled.lean, line 160](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/CorrelationInequalities/ReimerDoubled.lean#L160). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/reimer-inequality/doubled-ground-set-in-reimer-s-proof/index.html#double-compress).

## Family closed under erasing the left copy

`IsDownAtLeft i 𝒜`: `𝒜` is closed under erasing `inl i`.

Formalized by `StatMech.IsDownAtLeft`, a definition declared in [MathlibExt/Probability/CorrelationInequalities/ReimerDoubled.lean, line 170](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/CorrelationInequalities/ReimerDoubled.lean#L170). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/reimer-inequality/doubled-ground-set-in-reimer-s-proof/index.html#is-down-at-left).

## Family closed under inserting the right copy

`IsUpAtRight i 𝒜`: `𝒜` is closed under inserting `inr i`.

Formalized by `StatMech.IsUpAtRight`, a definition declared in [MathlibExt/Probability/CorrelationInequalities/ReimerDoubled.lean, line 174](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/CorrelationInequalities/ReimerDoubled.lean#L174). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/reimer-inequality/doubled-ground-set-in-reimer-s-proof/index.html#is-up-at-right).

## Left copy in the doubled ground set

The left copy `{inl a}` of `α` in `α ⊕ α`.

Formalized by `StatMech.leftBlock`, a definition declared in [MathlibExt/Probability/CorrelationInequalities/ReimerDoubledEvents.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/CorrelationInequalities/ReimerDoubledEvents.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/reimer-inequality/doubled-ground-set-in-reimer-s-proof/index.html#left-block).

## Right copy in the doubled ground set

The right copy `{inr a}` of `α` in `α ⊕ α`.

Formalized by `StatMech.rightBlock`, a definition declared in [MathlibExt/Probability/CorrelationInequalities/ReimerDoubledEvents.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/CorrelationInequalities/ReimerDoubledEvents.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/reimer-inequality/doubled-ground-set-in-reimer-s-proof/index.html#right-block).

## Restriction of a doubled configuration to the left copy

The restriction of a configuration on `α ⊕ α` to the left copy.

Formalized by `StatMech.leftCfg`, a definition declared in [MathlibExt/Probability/CorrelationInequalities/ReimerDoubledEvents.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/CorrelationInequalities/ReimerDoubledEvents.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/reimer-inequality/doubled-ground-set-in-reimer-s-proof/index.html#left-cfg).

## Restriction of a doubled configuration to the right copy

The restriction of a configuration on `α ⊕ α` to the right copy.

Formalized by `StatMech.rightCfg`, a definition declared in [MathlibExt/Probability/CorrelationInequalities/ReimerDoubledEvents.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/CorrelationInequalities/ReimerDoubledEvents.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/reimer-inequality/doubled-ground-set-in-reimer-s-proof/index.html#right-cfg).

## Event on the left copy of the doubled ground set

The event on `α ⊕ α` that the left restriction lies in `A`.

Formalized by `StatMech.leftEvent`, a definition declared in [MathlibExt/Probability/CorrelationInequalities/ReimerDoubledEvents.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/CorrelationInequalities/ReimerDoubledEvents.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/reimer-inequality/doubled-ground-set-in-reimer-s-proof/index.html#left-event).

## Event on the right copy of the doubled ground set

The event on `α ⊕ α` that the right restriction lies in `B`.

Formalized by `StatMech.rightEvent`, a definition declared in [MathlibExt/Probability/CorrelationInequalities/ReimerDoubledEvents.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/CorrelationInequalities/ReimerDoubledEvents.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/reimer-inequality/doubled-ground-set-in-reimer-s-proof/index.html#right-event).

## Doubled coordinate weight

The coordinate weight `w` on both copies of `α`.

Formalized by `StatMech.doubleWeight`, a definition declared in [MathlibExt/Probability/CorrelationInequalities/ReimerDoubledEvents.lean, line 123](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/CorrelationInequalities/ReimerDoubledEvents.lean#L123). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/reimer-inequality/doubled-ground-set-in-reimer-s-proof/index.html#double-weight).

## Reimer equality for a left event and a right event

Reimer's inequality, with equality, for a left event and a right event.

Formalized by `StatMech.reimer_wprob_doubled_split`, a theorem declared in [MathlibExt/Probability/CorrelationInequalities/ReimerDoubledEvents.lean, line 232](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/CorrelationInequalities/ReimerDoubledEvents.lean#L232). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/reimer-inequality/doubled-ground-set-in-reimer-s-proof/index.html#reimer-wprob-doubled-split).

## Weighted disjoint pairs as a doubled-weight probability

`wdpairs w 𝒜 ℬ` is the doubled-weight probability of `familyEvent (boxDoubled 𝒜 ℬ)`.

Formalized by `StatMech.wprob_familyEvent_boxDoubled_eq_wdpairs`, a theorem declared in [MathlibExt/Probability/CorrelationInequalities/ReimerDoubledEvents.lean, line 291](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/CorrelationInequalities/ReimerDoubledEvents.lean#L291). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/reimer-inequality/doubled-ground-set-in-reimer-s-proof/index.html#wprob-family-event-box-doubled-eq-wdpair).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Doubled ground set in Reimer's proof](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/reimer-inequality/doubled-ground-set-in-reimer-s-proof/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Probability/correlation-inequalities/reimer-inequality/doubled-ground-set-in-reimer-s-proof)
