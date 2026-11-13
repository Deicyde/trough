---
declaration: section
origin: cited
lean: Sk_of_le_power_aleph0, exists_gsetsBelowCutoff, Sk_leftRegular, Sk_prod, Sk_sum, Sk_fibreProduct, Sk_pushout, Sk_sigma
statement: formalized
proof: formalized
---

# 3.10 Sets with group action

Section 3.10 of the Stacks Project, [Tag 000T](https://stacks.math.columbia.edu/tag/000T). 2 tags here are carried by 10 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 000U, a lemma

[Tag 000U](https://stacks.math.columbia.edu/tag/000U) in the Stacks Project.

**`Sk_of_le_power_aleph0`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/GroupTheory/GroupAction/SizeCutoff.lean, line 305](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/GroupTheory/GroupAction/SizeCutoff.lean#L305). The attribute's comment: “(2)”.

> **Stacks 000U (2).** For an admissible cutoff `κ`, if `S` is an object of `G-Sets_α`
> and `T` is a `G`-set with `size T ≤ Bound(size S) = size(S) ^ ℵ₀`, then `T` is an object of
> `G-Sets_α`. This is condition `B2` of `AdmissibleBound` read through `Sk`.

```lean
theorem Sk_of_le_power_aleph0 {G : Type u} {κ : Cardinal.{u}} (hκ : AdmissibleBound G κ)
    {S T : Type u} (hS : Sk G κ S) (hT : gsetSize G T ≤ gsetSize G S ^ ℵ₀) : Sk G κ T
```

**`exists_gsetsBelowCutoff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/GroupTheory/GroupAction/SizeCutoff.lean, line 453](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/GroupTheory/GroupAction/SizeCutoff.lean#L453).

> **Stacks 000U.** For every group `G` and every family `S₀` of `G`-sets there is an admissible
> cutoff `κ`, a strong limit cardinal (the counterpart of the source's limit ordinal `α`), such
> that the full subcategory `G-Sets_α = gsetsBelowCutoff G κ` of `G-Sets = Action (Type u) G`
> satisfies:
> 1. every member of `S₀` and the left regular `G`-set `{}_G G` are objects of `G-Sets_α`;
> 2. every `G`-set `T` with `size T ≤ Bound(size S) = size(S) ^ ℵ₀` for some object `S` of
>    `G-Sets_α` is an object of `G-Sets_α`;
> 3. for every countable index category `J`, every functor `J ⥤ G-Sets_α` has a limit and a
>    colimit in `G-Sets_α`, and the inclusion into `G-Sets` preserves them.
>
> Objects of `G-Sets_α` are modelled up to isomorphism, by their size, since Mathlib has no
> cumulative hierarchy `V_α`; in particular clause (1) holds up to isomorphism.

```lean
theorem exists_gsetsBelowCutoff (G : Type u) [Group G] {ι : Type u}
    (S₀ : ι → Action (Type u) G) :
    ∃ κ : Cardinal.{u}, Cardinal.IsStrongPrelimit κ ∧ AdmissibleBound G κ ∧
      (∀ i, gsetsBelowCutoff G κ (S₀ i)) ∧ gsetsBelowCutoff G κ (Action.ofMulAction G G) ∧
      (∀ S T : Action (Type u) G, gsetsBelowCutoff G κ S →
        gsetSize G T.V ≤ gsetSize G S.V ^ ℵ₀ → gsetsBelowCutoff G κ T) ∧
      ∀ (J : Type v) [Category.{w} J] [CountableCategory J],
        HasLimitsOfShape J (gsetsBelowCutoff G κ).FullSubcategory ∧
          HasColimitsOfShape J (gsetsBelowCutoff G κ).FullSubcategory ∧
          PreservesLimitsOfShape J (gsetsBelowCutoff G κ).ι ∧
          PreservesColimitsOfShape J (gsetsBelowCutoff G κ).ι
```

## Tag 000V, a lemma

[Tag 000V](https://stacks.math.columbia.edu/tag/000V) in the Stacks Project.

**`Sk_leftRegular`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/GroupTheory/GroupAction/SizeCutoff.lean, line 216](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/GroupTheory/GroupAction/SizeCutoff.lean#L216). The attribute's comment: “(1)”.

> **Stacks 000V (1)**. The left regular `G`-set `{}_G G` is an object of `G-Sets_α`, since
> its size is `max {ℵ₀, #G}`, which is below the cutoff by `B1`.

```lean
theorem Sk_leftRegular (G : Type u) [Group G] (κ : Cardinal.{u})
    (hκ : AdmissibleBound G κ) :
    Sk G κ G
```

**`Sk_prod`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/GroupTheory/GroupAction/SizeCutoff.lean, line 224](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/GroupTheory/GroupAction/SizeCutoff.lean#L224). The attribute's comment: “(2)”.

> **Stacks 000V (2)**. The product `S × T` of two `G`-sets below the cutoff, with the
> diagonal `G`-action, is again below it: `#(S × T) = #S * #T ≤ max {max {#S, #T}, ℵ₀} < κ`.

```lean
theorem Sk_prod (G : Type u) [Group G] (κ : Cardinal.{u})
    (hκ : AdmissibleBound G κ) (S T : Type u) [MulAction G S] [MulAction G T]
    (hS : Sk G κ S) (hT : Sk G κ T) :
    Sk G κ (S × T)
```

**`Sk_sum`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/GroupTheory/GroupAction/SizeCutoff.lean, line 234](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/GroupTheory/GroupAction/SizeCutoff.lean#L234). The attribute's comment: “(2)”.

> **Stacks 000V (2)**. The coproduct `S ⊕ T` of two `G`-sets below the cutoff, with the
> disjoint-union `G`-action, is again below it:
> `#(S ⊕ T) = #S + #T ≤ max {max {#S, #T}, ℵ₀} < κ`.

```lean
theorem Sk_sum (G : Type u) [Group G] (κ : Cardinal.{u})
    (hκ : AdmissibleBound G κ) (S T : Type u) [MulAction G S] [MulAction G T]
    (hS : Sk G κ S) (hT : Sk G κ T) :
    Sk G κ (S ⊕ T)
```

**`Sk_fibreProduct`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/GroupTheory/GroupAction/SizeCutoff.lean, line 244](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/GroupTheory/GroupAction/SizeCutoff.lean#L244). The attribute's comment: “(2)”.

> **Stacks 000V (2)**. For `G`-sets `S`, `T`, `R` below the cutoff and equivariant maps
> `f : S → R`, `h : T → R`, the fibre product `S ×_R T = {p : S × T // f p.1 = h p.2}` is
> below the cutoff, being a subtype of `S × T`.

```lean
theorem Sk_fibreProduct (G : Type u) [Group G] (κ : Cardinal.{u})
    (hκ : AdmissibleBound G κ) (S T R : Type u)
    [MulAction G S] [MulAction G T] [MulAction G R]
    (hS : Sk G κ S) (hT : Sk G κ T)
    (f : S → R) (h : T → R) :
    Sk G κ { p : S × T // f p.1 = h p.2 }
```

**`Sk_pushout`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/GroupTheory/GroupAction/SizeCutoff.lean, line 257](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/GroupTheory/GroupAction/SizeCutoff.lean#L257). The attribute's comment: “(2)”.

> **Stacks 000V (2)**. For `G`-sets `S`, `T`, `R` below the cutoff and equivariant maps
> `f : R → S`, `h : R → T`, the pushout of `S ← R → T` is below the cutoff, being a quotient
> of `S ⊕ T`. The pushout is modelled as the quotient of `S ⊕ T` by the equivalence relation
> generated by `inl (f r) ~ inr (h r)`.

```lean
theorem Sk_pushout (G : Type u) [Group G] (κ : Cardinal.{u})
    (hκ : AdmissibleBound G κ) (S T R : Type u)
    [MulAction G S] [MulAction G T] [MulAction G R]
    (hS : Sk G κ S) (hT : Sk G κ T)
    (f : R → S) (h : R → T) :
    Sk G κ
      (Quotient
        (Relation.EqvGen.setoid
          (fun a b : S ⊕ T =>
            ∃ r : R, a = Sum.inl (f r) ∧ b = Sum.inr (h r))))
```

**`Sk_sigma`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/GroupTheory/GroupAction/SizeCutoff.lean, line 274](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/GroupTheory/GroupAction/SizeCutoff.lean#L274). The attribute's comment: “(2)”.

> **Stacks 000V (2)**. For an at-most-countable index type `ι` and a family of `G`-sets
> `S i` below the cutoff, the coproduct `Σ i, S i` with the fibrewise `G`-action is below the
> cutoff: `#(Σ i, S i) = Σ i, #(S i) ≤ #ι * ⨆ i, #(S i)`, and a supremum of at most `ℵ₀` many
> cardinals below `κ` is below `κ` because `κ.ord` has uncountable cofinality (`B3`).

```lean
theorem Sk_sigma (G : Type u) [Group G] (κ : Cardinal.{u})
    (hκ : AdmissibleBound G κ) (ι : Type u) (hι : #ι ≤ ℵ₀)
    (S : ι → Type u) [∀ i, MulAction G (S i)] (hS : ∀ i, Sk G κ (S i)) :
    Sk G κ (Σ i, S i)
```

**`Sk_pi`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/GroupTheory/GroupAction/SizeCutoff.lean, line 286](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/GroupTheory/GroupAction/SizeCutoff.lean#L286). The attribute's comment: “(2)”.

> **Stacks 000V (2)**. For an at-most-countable index type `ι` and a family of `G`-sets
> `S i` below the cutoff, the product `Π i, S i` with the pointwise `G`-action is below the
> cutoff: writing `s = ⨆ i, #(S i)`, which is below `κ` by `B3`, one has
> `#(Π i, S i) = Π i, #(S i) ≤ s ^ #ι ≤ s ^ ℵ₀ < κ` by `B2`. If `s = 0` the bound is instead
> the trivial `s ^ #ι ≤ 1 < ℵ₀ < κ`.

```lean
theorem Sk_pi (G : Type u) [Group G] (κ : Cardinal.{u})
    (hκ : AdmissibleBound G κ) (ι : Type u) (hι : #ι ≤ ℵ₀)
    (S : ι → Type u) [∀ i, MulAction G (S i)] (hS : ∀ i, Sk G κ (S i)) :
    Sk G κ (∀ i, S i)
```

**`Sk_subtype`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/GroupTheory/GroupAction/SizeCutoff.lean, line 295](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/GroupTheory/GroupAction/SizeCutoff.lean#L295). The attribute's comment: “(3)”.

> **Stacks 000V (3)**. For a `G`-set `U` below the cutoff and a `G`-stable subset `O ⊆ U`,
> the induced `G`-set on `{x : U // x ∈ O}` is below the cutoff, being a subtype of `U`.

```lean
theorem Sk_subtype (G : Type u) [Group G] (κ : Cardinal.{u})
    (hκ : AdmissibleBound G κ) (U : Type u) [MulAction G U]
    (hU : Sk G κ U) (O : Set U) :
    Sk G κ { x : U // x ∈ O }
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 3.10, Tag 000T](https://stacks.math.columbia.edu/tag/000T)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
