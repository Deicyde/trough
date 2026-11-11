---
declaration: section
origin: cited
lean: TopCat.Presheaf.section_ext, TopCat.Presheaf.IsSeparated', alphaX_bijective, cX_bijective, betaX_bijective, stalkEquivSmoothGerm, statement1_exists_evalMap, statement2_empty_stalk
statement: formalized
proof: formalized
---

# 6.11 Stalks

Section 6.11 of the Stacks Project, [Tag 0078](https://stacks.math.columbia.edu/tag/0078). 5 tags here are carried by 8 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0079, a lemma

[Tag 0079](https://stacks.math.columbia.edu/tag/0079) in the Stacks Project.

Declarations registered for the tag:

- [`TopCat.Presheaf.section_ext`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=TopCat.Presheaf.section_ext#doc) registered with `add_to_stacks` in [StacksFrontier/Topology/Sheaves/Stalk/Injective.lean, line 22](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Stalk/Injective.lean#L22) (StacksFrontier): “two sections with the same germ at every point of `U` are equal”. References: SGA 2 XIV (1.8.2.1), “Zariski case”.

## Tag 007A, a definition

[Tag 007A](https://stacks.math.columbia.edu/tag/007A) in the Stacks Project.

**`TopCat.Presheaf.IsSeparated'`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Stalk/Separated.lean, line 78](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Stalk/Separated.lean#L78). References: SGA 3 IV (4.3.1), “special case”; SGA 3 IV (4.3.18), “special case”; SGA 4 II (2.1), “special case”.

> A presheaf of sets `F` on a topological space `X` is *separated* if for
> every open subset `U ⊆ X`, the canonical map sending a section to the
> family of its germs at the points of `U` is injective.

```lean
def IsSeparated' : Prop
```

## Tag 007B, an example

[Tag 007B](https://stacks.math.columbia.edu/tag/007B) in the Stacks Project.

**`alphaX_bijective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Stalk/Constant.lean, line 94](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Stalk/Constant.lean#L94).

> The canonical bijection `A = (A_p)_x`: the map `α_x : A → (A_p)_x` is bijective.

```lean
theorem alphaX_bijective : Function.Bijective (alphaX X A x)
```

**`cX_bijective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Stalk/Constant.lean, line 134](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Stalk/Constant.lean#L134).

> The map on stalks `c_x : (A_p)_x → A̲_x` induced by functoriality from `c : A_p → A̲` is a
> bijection.

```lean
theorem cX_bijective : Function.Bijective (cX X A x)
```

**`betaX_bijective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Stalk/Constant.lean, line 144](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Stalk/Constant.lean#L144).

> The canonical bijection `A = A̲_x`: the composite `β_x := c_x ∘ α_x : A → A̲_x` is
> bijective.

```lean
theorem betaX_bijective : Function.Bijective (betaX X A x)
```

## Tag 007C, an example

[Tag 007C](https://stacks.math.columbia.edu/tag/007C) in the Stacks Project.

**`stalkEquivSmoothGerm`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Stalk/SmoothFunctions.lean, line 285](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Stalk/SmoothFunctions.lean#L285).

> **Main theorem (Stacks 007C).** For `X = ℝ^n` with the Euclidean topology
> and `C^∞_{ℝ^n}` the presheaf of `C^∞` real-valued functions, the stalk at a
> point `x ∈ ℝ^n` is in bijection with the type of smooth germs at `x`, that is,
> equivalence classes of `C^∞` functions defined on open neighbourhoods of `x`
> modulo eventual equality.

```lean
noncomputable def stalkEquivSmoothGerm (n : ℕ) (x : RealN n) :
    (smoothPresheaf n).stalk (X := TopCat.of (RealN n)) x ≃ SmoothGerm n x
```

## Tag 007D, an example

[Tag 007D](https://stacks.math.columbia.edu/tag/007D) in the Stacks Project.

**`statement1_exists_evalMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Stalk/Product.lean, line 126](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Stalk/Product.lean#L126). The attribute's comment: “(1)”.

> **Stacks 007D (1).** For every `x ∈ X` there is a well-defined function
> `π_x : F_x → A x` with `π_x (germ s) = s x` for every section `s` of the product sheaf over a
> neighbourhood of `x`.

```lean
theorem statement1_exists_evalMap (x : X) :
    ∃ π : (presheafToTypes X A).stalk x → A x,
      ∀ (U : Opens X) (hx : x ∈ U) (s : ∀ y : U, A y),
        π ((presheafToTypes X A).germ U x hx s) = s ⟨x, hx⟩
```

**`statement2_empty_stalk`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Stalk/Product.lean, line 159](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Stalk/Product.lean#L159). The attribute's comment: “(2)”.

> **Stacks 007D (2).** Fix `x`. If every open neighbourhood `U` of `x` contains a point
> `y ∈ U` with `A y` empty, then the stalk `F_x` is empty.

```lean
theorem statement2_empty_stalk (x : X)
    (h : ∀ U : Opens X, x ∈ U → ∃ y : X, ∃ _ : y ∈ U, IsEmpty (A y)) :
    IsEmpty ((presheafToTypes X A).stalk x)
```

**`statement3_surjects_onto_tails`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Stalk/Product.lean, line 272](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Stalk/Product.lean#L272). The attribute's comment: “(3)”.

> **Stacks 007D (3).** Suppose `A y = {0,1}` for all `y` (here `A = fun _ => Fin 2`), the
> points `x n` are pairwise distinct, and `x n → x` in the sense that every open neighbourhood
> of `x` contains `x n` for all but finitely many `n`. Then there is a well-defined map
> `τ : F_x → T` sending the germ of a section `s` over `U` to the tail class of `b^{(U,s)}`,
> and `τ` is surjective; moreover `T` is infinite.

```lean
theorem statement3_surjects_onto_tails
    (xseq : ℕ → X) (x : X)
    (hdist : Function.Injective xseq)
    (hconv : ∀ U : Opens X, x ∈ U → {n | xseq n ∉ U}.Finite) :
    (∃ τ : (presheafToTypes X (fun _ : X => Fin 2)).stalk x → Tails,
      (∀ (U : Opens X) (hx : x ∈ U) (s : ∀ _ : U, Fin 2),
        τ ((presheafToTypes X (fun _ : X => Fin 2)).germ U x hx s)
          = Quotient.mk tailSetoid (tauSeq xseq U s)) ∧
      Function.Surjective τ)
    ∧ Infinite Tails
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 6.11, Tag 0078](https://stacks.math.columbia.edu/tag/0078)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
