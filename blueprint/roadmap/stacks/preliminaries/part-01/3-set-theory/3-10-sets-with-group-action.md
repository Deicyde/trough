---
declaration: section
origin: cited
lean: Sk_of_le_power_aleph0, exists_admissibleBound, Sk_leftRegular, Sk_prod, Sk_sum, Sk_fibreProduct, Sk_pushout, Sk_sigma
statement: formalized
proof: formalized
---

# 3.10 Sets with group action

Section 3.10 of the Stacks Project, [Tag 000T](https://stacks.math.columbia.edu/tag/000T). 2 tags here are carried by 10 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 000U, a lemma

[Tag 000U](https://stacks.math.columbia.edu/tag/000U) in the Stacks Project.

**`Sk_of_le_power_aleph0`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/GroupTheory/GroupAction/SizeCutoff.lean, line 286](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/GroupTheory/GroupAction/SizeCutoff.lean#L286). The attribute's comment: “(2)”.

> **Stacks 000U (2).** For an admissible cutoff `κ`, if `S` is an object of `G-Sets_α`
> and `T` is a `G`-set with `size T ≤ Bound(size S) = size(S) ^ ℵ₀`, then `T` is an object of
> `G-Sets_α`. This is condition `B2` of `AdmissibleBound` read through `Sk`.

```lean
theorem Sk_of_le_power_aleph0 {G : Type u} {κ : Cardinal.{u}} (hκ : AdmissibleBound G κ)
    {S T : Type u} (hS : Sk G κ S) (hT : gsetSize G T ≤ gsetSize G S ^ ℵ₀) : Sk G κ T
```

**`exists_admissibleBound`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/GroupTheory/GroupAction/SizeCutoff.lean, line 299](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/GroupTheory/GroupAction/SizeCutoff.lean#L299).

> **Stacks 000U.** For every group `G` and every family `S₀` of `G`-sets there is a
> cardinal `κ` which is an admissible cutoff for `G` and for which every member of `S₀`, as
> well as the left regular `G`-set `{}_G G`, is an object of `G-Sets_α`; moreover `G-Sets_α`
> is closed under `G`-sets of size at most `Bound` of the size of one of its objects.
>
> `Cardinal.IsStrongPrelimit κ` records that `κ` is a limit cardinal, the counterpart of the
> source's "`α` is a limit ordinal"; it is also what gives condition `B2` of
> `AdmissibleBound`.

```lean
theorem exists_admissibleBound (G : Type u) {ι : Type u} (S₀ : ι → Type u) :
    ∃ κ : Cardinal.{u}, Cardinal.IsStrongPrelimit κ ∧ AdmissibleBound G κ ∧
      Sk G κ G ∧ (∀ i, Sk G κ (S₀ i)) ∧
      ∀ S T : Type u, Sk G κ S → gsetSize G T ≤ gsetSize G S ^ ℵ₀ → Sk G κ T
```

## Tag 000V, a lemma

[Tag 000V](https://stacks.math.columbia.edu/tag/000V) in the Stacks Project.

**`Sk_leftRegular`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/GroupTheory/GroupAction/SizeCutoff.lean, line 181](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/GroupTheory/GroupAction/SizeCutoff.lean#L181). The attribute's comment: “(1)”.

> **Stacks 000V (1)**. The left regular `G`-set `{}_G G` is an object of `G-Sets_α`, since
> its size is `max {ℵ₀, #G}`, which is below the cutoff by `B1`.

```lean
theorem Sk_leftRegular (G : Type u) [Group G] (κ : Cardinal.{u})
    (hκ : AdmissibleBound G κ) :
    Sk G κ G
```

**`Sk_prod`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/GroupTheory/GroupAction/SizeCutoff.lean, line 189](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/GroupTheory/GroupAction/SizeCutoff.lean#L189). The attribute's comment: “(2)”.

> **Stacks 000V (2)**. The product `S × T` of two `G`-sets below the cutoff, with the
> diagonal `G`-action, is again below it: `#(S × T) = #S * #T ≤ max {max {#S, #T}, ℵ₀} < κ`.

```lean
theorem Sk_prod (G : Type u) [Group G] (κ : Cardinal.{u})
    (hκ : AdmissibleBound G κ) (S T : Type u) [MulAction G S] [MulAction G T]
    (hS : Sk G κ S) (hT : Sk G κ T) :
    Sk G κ (S × T)
```

**`Sk_sum`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/GroupTheory/GroupAction/SizeCutoff.lean, line 199](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/GroupTheory/GroupAction/SizeCutoff.lean#L199). The attribute's comment: “(2)”.

> **Stacks 000V (2)**. The coproduct `S ⊕ T` of two `G`-sets below the cutoff, with the
> disjoint-union `G`-action, is again below it:
> `#(S ⊕ T) = #S + #T ≤ max {max {#S, #T}, ℵ₀} < κ`.

```lean
theorem Sk_sum (G : Type u) [Group G] (κ : Cardinal.{u})
    (hκ : AdmissibleBound G κ) (S T : Type u) [MulAction G S] [MulAction G T]
    (hS : Sk G κ S) (hT : Sk G κ T) :
    Sk G κ (S ⊕ T)
```

**`Sk_fibreProduct`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/GroupTheory/GroupAction/SizeCutoff.lean, line 209](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/GroupTheory/GroupAction/SizeCutoff.lean#L209). The attribute's comment: “(2)”.

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

**`Sk_pushout`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/GroupTheory/GroupAction/SizeCutoff.lean, line 222](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/GroupTheory/GroupAction/SizeCutoff.lean#L222). The attribute's comment: “(2)”.

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

**`Sk_sigma`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/GroupTheory/GroupAction/SizeCutoff.lean, line 239](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/GroupTheory/GroupAction/SizeCutoff.lean#L239). The attribute's comment: “(2)”.

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

**`Sk_pi`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/GroupTheory/GroupAction/SizeCutoff.lean, line 256](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/GroupTheory/GroupAction/SizeCutoff.lean#L256). The attribute's comment: “(2)”.

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

**`Sk_subtype`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/GroupTheory/GroupAction/SizeCutoff.lean, line 276](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/GroupTheory/GroupAction/SizeCutoff.lean#L276). The attribute's comment: “(3)”.

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
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
