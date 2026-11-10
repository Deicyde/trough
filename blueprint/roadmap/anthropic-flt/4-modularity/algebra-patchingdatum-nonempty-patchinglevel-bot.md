---
declaration: theorem
origin: cited
lean: Algebra.PatchingDatum.nonempty_patchingLevel_bot
statement: formalized
proof: formalized
---

# Algebra.PatchingDatum.nonempty_patchingLevel_bot

```lean
theorem Algebra.PatchingDatum.nonempty_patchingLevel_bot
    {𝒪 : Type} [CommRing 𝒪] [IsDomain 𝒪] [IsDiscreteValuationRing 𝒪]
    [IsAdicComplete (IsLocalRing.maximalIdeal 𝒪) 𝒪] [Finite (IsLocalRing.ResidueField 𝒪)]
    {ℓ r : ℕ} (hℓ : (ℓ : 𝒪) ∈ IsLocalRing.maximalIdeal 𝒪)
    {R : Type} [CommRing R] [Algebra 𝒪 R] {M : Type} [AddCommGroup M] [Module R M]
    (P : Algebra.PatchingDatum 𝒪 ℓ r R M) :
    Nonempty (Algebra.PatchingLevel 𝒪 r R M ⊥)
```

*Quoted from [Theorems/Thm_Algebra_PatchingDatum_nonempty_patchingLevel_bot.lean, line 7](https://github.com/anthropics/fermats-last-theorem/blob/6e837e75355538c7f80bab5b956861e86c4eacc2/Theorems/Thm_Algebra_PatchingDatum_nonempty_patchingLevel_bot.lean#L7) of [anthropics/fermats-last-theorem](https://github.com/anthropics/fermats-last-theorem) at commit [6e837e75](https://github.com/anthropics/fermats-last-theorem/tree/6e837e75355538c7f80bab5b956861e86c4eacc2), Apache-2.0: the file's text from the end of its imports and `attribute` lines to the top-level `:=`.*

Aliases on the repository's web pages: “Taylor-Wiles patching”, “patching datum”.

## Depends on

The repository's citation graph records the theorems each proof cites, not what statements use, so no statement dependencies are listed.

## Lean

`Algebra.PatchingDatum.nonempty_patchingLevel_bot`, stated in [Theorems/Thm_Algebra_PatchingDatum_nonempty_patchingLevel_bot.lean, line 7](https://github.com/anthropics/fermats-last-theorem/blob/6e837e75355538c7f80bab5b956861e86c4eacc2/Theorems/Thm_Algebra_PatchingDatum_nonempty_patchingLevel_bot.lean#L7) and proved in [P2M/Sol/S_Algebra_PatchingDatum_nonempty_patchingLevel_bot.lean](https://github.com/anthropics/fermats-last-theorem/blob/6e837e75355538c7f80bab5b956861e86c4eacc2/P2M/Sol/S_Algebra_PatchingDatum_nonempty_patchingLevel_bot.lean). Read at commit [6e837e75](https://github.com/anthropics/fermats-last-theorem/tree/6e837e75355538c7f80bab5b956861e86c4eacc2), without running Lean.

## Sources

- [Statement of `Algebra.PatchingDatum.nonempty_patchingLevel_bot` in Theorems/Thm_Algebra_PatchingDatum_nonempty_patchingLevel_bot.lean](https://github.com/anthropics/fermats-last-theorem/blob/6e837e75355538c7f80bab5b956861e86c4eacc2/Theorems/Thm_Algebra_PatchingDatum_nonempty_patchingLevel_bot.lean#L7)
- [Proof of `Algebra.PatchingDatum.nonempty_patchingLevel_bot` in P2M/Sol/S_Algebra_PatchingDatum_nonempty_patchingLevel_bot.lean](https://github.com/anthropics/fermats-last-theorem/blob/6e837e75355538c7f80bab5b956861e86c4eacc2/P2M/Sol/S_Algebra_PatchingDatum_nonempty_patchingLevel_bot.lean)
- [The repository's documentation page for `Algebra.PatchingDatum.nonempty_patchingLevel_bot`](https://tianyipeng.github.io/fermats-last-theorem/thm.html#Algebra.PatchingDatum.nonempty_patchingLevel_bot)
