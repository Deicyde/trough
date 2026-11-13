---
declaration: section
origin: cited
lean: Ordinal.exists_factorization_of_mk_lt_cof, Cardinal.exists_ordinal_cof_gt
statement: formalized
proof: formalized
---

# 3.7 Cofinality

Section 3.7 of the Stacks Project, [Tag 000E](https://stacks.math.columbia.edu/tag/000E). 2 tags here are carried by 2 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 05N2, a lemma

[Tag 05N2](https://stacks.math.columbia.edu/tag/05N2) in the Stacks Project.

**`Ordinal.exists_factorization_of_mk_lt_cof`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/SetTheory/Cardinal/Cofinality.lean, line 78](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/SetTheory/Cardinal/Cofinality.lean#L78).

> **Stacks 05N2.** Let `β` be an ordinal and `(F_α)_{α < β}` an ordinal-indexed direct
> system with colimit `DirectLimit F f` and canonical maps `ι_α : F_α → DirectLimit F f`,
> `x ↦ ⟦⟨α, x⟩⟧`. Let `S` be a set and `φ : S → DirectLimit F f` a function. If the
> cofinality of `β` exceeds the cardinality of `S`, then `φ` factors through a single stage:
> there are an `α < β` and a `φ_α : S → F_α` with `ι_α ∘ φ_α = φ`.

```lean
theorem exists_factorization_of_mk_lt_cof {β : Ordinal.{u}}
    {F : {α : Ordinal.{u} // α < β} → Type u}
    {T : ∀ ⦃i j : {α : Ordinal.{u} // α < β}⦄, i ≤ j → Sort v}
    (f : ∀ i j (h : i ≤ j), T h)
    [∀ ⦃i j : {α : Ordinal.{u} // α < β}⦄ (h : i ≤ j), FunLike (T h) (F i) (F j)]
    [DirectedSystem F (f · · ·)]
    {S : Type u} (φ : S → DirectLimit F f)
    (hcof : Cardinal.mk S < β.cof) :
    ∃ (i : {α : Ordinal.{u} // α < β}) (φi : S → F i),
      (fun s => (⟦⟨i, φi s⟩⟧ : DirectLimit F f)) = φ
```

## Tag 05N3, a proposition

[Tag 05N3](https://stacks.math.columbia.edu/tag/05N3) in the Stacks Project.

**`Cardinal.exists_ordinal_cof_gt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/SetTheory/Cardinal/Cofinality.lean, line 61](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/SetTheory/Cardinal/Cofinality.lean#L61).

> **Stacks 05N3.** For every cardinal `κ` there is an ordinal `α` with `κ < cf(α)`:
> the successor of the infinite cardinal `κ ⊔ ℵ₀` is regular, so the ordinal it indexes has
> cofinality `(κ ⊔ ℵ₀)⁺`, which is strictly greater than `κ`.

```lean
theorem exists_ordinal_cof_gt (κ : Cardinal) : ∃ α : Ordinal, κ < α.cof
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 3.7, Tag 000E](https://stacks.math.columbia.edu/tag/000E)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
