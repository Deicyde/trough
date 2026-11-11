---
declaration: section
origin: cited
lean: ChainComplex.shiftFunctor, ChainComplex.shiftIso, Homotopy.equivHomShiftChain, Homotopy.equivHomShiftChainSelf, ChainComplex.homOfDegreewiseSplit, ChainComplex.homOfDegreewiseSplit_f, ChainComplex.homologyMap_homOfDegreewiseSplit, ChainComplex.homotopyHomOfDegreewiseSplit
statement: formalized
proof: formalized
---

# 12.14 Homotopy and the shift functor

Section 12.14 of the Stacks Project, [Tag 0119](https://stacks.math.columbia.edu/tag/0119). 12 tags here are carried by 13 declarations of the repository (12 in StacksCore and 1 in StacksFrontier) and 9 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 011A, a definition

[Tag 011A](https://stacks.math.columbia.edu/tag/011A) in the Stacks Project.

**`ChainComplex.shiftFunctor`**, an abbrev in StacksCore (human-reviewed), declared in [StacksCore/Algebra/Homology/HomotopyCategory/Shift.lean, line 84](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Algebra/Homology/HomotopyCategory/Shift.lean#L84). The attribute's comment: “the definition, together with its three `@[simps]` clauses below”.

> **Stacks 011A.** The shift functor by `n : ℤ` on `ChainComplex C ℤ`, sending a chain complex
> `K` to the complex which is `K.X (i + n)` in degree `i` and whose differentials are those of `K`
> multiplied by `(-1)^n`.
>
> This mirrors `CochainComplex.shiftFunctor`, which Mathlib has and which is tag 011G; the two
> definitions differ only in the complex shape and in the arithmetic discharging `shape`.

```lean
abbrev shiftFunctor (n : ℤ) : ChainComplex C ℤ ⥤ ChainComplex C ℤ
```

## Tag 011B, a definition

[Tag 011B](https://stacks.math.columbia.edu/tag/011B) in the Stacks Project.

**`ChainComplex.shiftIso`**, a def in StacksCore (human-reviewed), declared in [StacksCore/Algebra/Homology/HomotopyCategory/Shift.lean, line 276](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Algebra/Homology/HomotopyCategory/Shift.lean#L276). The attribute's comment: “the identification; the Stacks arrow `H_{i+k}(A_•) → H_i(A[k]_•)` is its `inv`”.

> **Stacks 011B.** For `k : ℤ` the identification `H_{i+k}(A_•) = H_i(A[k]_•)` coming from
> `A_{i+k} = A[k]_i`, as an isomorphism of functors.
>
> As for its cochain twin 011H, Mathlib's direction is the opposite of the Stacks project's: the
> `hom` component runs `H_a(K[n]) ⟶ H_{a'}(K)` for `a + n = a'`, so the arrow the Stacks project
> writes is `inv`. Being an isomorphism it carries the tag either way.
>
> No sign enters, even though the shift multiplies differentials by `(-1)^k`: in
> `shiftShortComplexFunctor'` the sign sits on the outer two terms and homology is the subquotient
> cut out by the middle one.

```lean
noncomputable def shiftIso (n a a' : ℤ) (ha' : a + n = a') :
    CategoryTheory.shiftFunctor (ChainComplex C ℤ) n ⋙
        homologyFunctor C (ComplexShape.down ℤ) a ≅
      homologyFunctor C (ComplexShape.down ℤ) a'
```

## Tag 011C, a lemma

[Tag 011C](https://stacks.math.columbia.edu/tag/011C) in the Stacks Project.

**`Homotopy.equivHomShiftChain`**, a def in StacksCore (human-reviewed), declared in [StacksCore/Algebra/Homology/HomotopyCategory/HomotopyShift.lean, line 107](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Algebra/Homology/HomotopyCategory/HomotopyShift.lean#L107).

> **Stacks 011C**, second sentence. Given one homotopy `h₀` from `a` to `b`, the homotopies from
> `a` to `b` correspond to the morphisms of complexes `A_• ⟶ B[1]_•`, by `h ↦ h - h₀`. Together with
> the fact that the target is a group, this is the assertion that the homotopies from `a` to `b`
> form a principal homogeneous space under it whenever they are nonempty.

```lean
def equivHomShiftChain (h₀ : Homotopy a b) : Homotopy a b ≃ (A ⟶ B⟦(1 : ℤ)⟧)
```

**`Homotopy.equivHomShiftChainSelf`**, a def in StacksCore (human-reviewed), declared in [StacksCore/Algebra/Homology/HomotopyCategory/HomotopyShift.lean, line 126](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Algebra/Homology/HomotopyCategory/HomotopyShift.lean#L126). The attribute's comment: “first sentence, the `b = a` case based at the zero homotopy”.

> **Stacks 011C**, first sentence. The self-homotopies of `a` correspond to the morphisms of
> complexes `A_• ⟶ B[1]_•`.

```lean
def equivHomShiftChainSelf (a : A ⟶ B) : Homotopy a a ≃ (A ⟶ B⟦(1 : ℤ)⟧)
```

## Tag 011D, a lemma

[Tag 011D](https://stacks.math.columbia.edu/tag/011D) in the Stacks Project.

**`ChainComplex.homOfDegreewiseSplit`**, a def in StacksCore (human-reviewed), declared in [StacksCore/Algebra/Homology/HomotopyCategory/ChainDegreewiseSplit.lean, line 135](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Algebra/Homology/HomotopyCategory/ChainDegreewiseSplit.lean#L135). The attribute's comment: “the morphism `δ(s) : C_• → A[-1]_•` itself.”.

> **Stacks 011D.** The morphism of complexes `δ(s) : C_• ⟶ A[-1]_•` attached to a degreewise
> split complex of chain complexes, with components `π_{n-1} ∘ d_{B,n} ∘ s_n` read in diagrammatic
> order.
>
> As for its cochain twin 011J, no exactness is needed: the splittings supply degreewise whatever
> the Stacks statement asks of the short exact sequence, so the hypotheses are `Preadditive` and a
> `ShortComplex`. The Stacks proof's trailing minus is supplied by `d_{A[-1]} = -d_A`, which is the
> `k = -1` case of the `(-1)^k` of 011A.

```lean
def homOfDegreewiseSplit : S.X₃ ⟶ S.X₁⟦(-1 : ℤ)⟧
```

**`ChainComplex.homOfDegreewiseSplit_f`**, a lemma in StacksCore (human-reviewed), declared in [StacksCore/Algebra/Homology/HomotopyCategory/ChainDegreewiseSplit.lean, line 150](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Algebra/Homology/HomotopyCategory/ChainDegreewiseSplit.lean#L150). The attribute's comment: “its components, `δ(s)_n = π_{n-1} ∘ d_{B,n} ∘ s_n`.”.

> The components of `δ(s)`, `δ(s)_n = π_{n-1} ∘ d_{B,n} ∘ s_n`. Writing the definition at the
> index `n - 1`, which is what `(ComplexShape.down ℤ).next` normalises to, makes this hold by `rfl`
> with no `XIsoOfEq` in sight.

```lean
lemma homOfDegreewiseSplit_f (n : ℤ) :
    (homOfDegreewiseSplit S σ).f n
      = sectionHom S σ n ≫ S.X₂.d n (n - 1) ≫ retractionHom S σ (n - 1)
```

## Tag 011E, a lemma

[Tag 011E](https://stacks.math.columbia.edu/tag/011E) in the Stacks Project.

**`ChainComplex.homologyMap_homOfDegreewiseSplit`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/Algebra/Homology/HomotopyCategory/ChainDegreewiseSplit.lean, line 260](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Algebra/Homology/HomotopyCategory/ChainDegreewiseSplit.lean#L260).

> **Stacks 011E.** The map `H_i(δ(s)) : H_i(C_•) ⟶ H_i(A[-1]_•) = H_{i-1}(A_•)` induced by the
> morphism `δ(s)` of 011D is the connecting morphism of the long exact homology sequence of 0111.
>
> There is no sign: the identification of 011B is the unsigned re-indexing, because the `(-1)^k` of
> the shift sits on the outer two terms of the short complex and homology is cut out by the middle
> one. The opposite convention is not merely unproved but false — it forces every such connecting
> map to be `2`-torsion.
>
> The identification is taken through `ChainComplex.homologyShiftIso` rather than through
> `Functor.shiftIso`, which would need a `(homologyFunctor C (ComplexShape.down ℤ) 0).ShiftSequence ℤ`
> instance that the chain side does not have. Registering one is possible but buys only spelling
> parity with the cochain twin 011K: `ChainComplex.shiftIso` already *is* the natural isomorphism
> the statement wants.

```lean
theorem homologyMap_homOfDegreewiseSplit (S : ShortComplex (ChainComplex C ℤ))
    (σ : ∀ n, (S.map (eval C (down ℤ) n)).Splitting) (hS : S.ShortExact)
    (i j : ℤ) (hij : (down ℤ).Rel i j) (h : i + -1 = j) :
    HomologicalComplex.homologyMap (homOfDegreewiseSplit S σ) i ≫
        (homologyShiftIso S.X₁ (-1) i j h).hom =
      hS.δ i j hij
```

## Tag 011F, a lemma

[Tag 011F](https://stacks.math.columbia.edu/tag/011F) in the Stacks Project.

**`ChainComplex.homotopyHomOfDegreewiseSplit`**, a def in StacksCore (human-reviewed), declared in [StacksCore/Algebra/Homology/HomotopyCategory/ChainDegreewiseSplit.lean, line 217](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Algebra/Homology/HomotopyCategory/ChainDegreewiseSplit.lean#L217).

> **Stacks 011F.** The family `h_n : C_n ⟶ A_n = A[-1]_{n+1}` is a homotopy between the
> morphisms `δ(s)` and `δ(s')` of 011D attached to two choices of splittings.
>
> Unlike its cochain twin 011L, this is stated with `h` and not with `g = -h`: a homotopy of chain
> complexes has components `C_n ⟶ D_{n+1}`, and going from `D = A` to `D = A[-1]` shifts by `-1`
> rather than by `+1`, which is the other sign. Concretely, `prevD` pairs `h_n` with
> `d_{A[-1],n+1} = -d_{A,n}`, and that minus is what turns 011L's `g` into 011F's `h`.

```lean
def homotopyHomOfDegreewiseSplit :
    Homotopy (homOfDegreewiseSplit S σ) (homOfDegreewiseSplit S σ')
```

## Tag 011G, a definition

[Tag 011G](https://stacks.math.columbia.edu/tag/011G) in the Stacks Project.

Declarations registered for the tag:

- [`CochainComplex.shiftFunctor`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CochainComplex.shiftFunctor#doc) registered with `add_to_stacks` in [StacksCore/Algebra/Homology/HomotopyCategory/Shift.lean, line 34](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Algebra/Homology/HomotopyCategory/Shift.lean#L34) (StacksCore): “the definition; Mathlib gives the shift for every `k : ℤ` at once, not for `k = 1` iterated, so the `(-1)^k` sign is definitional rather than derived.”. References: SGA 2 XIV (2.3); SGA 4 XVII (2.2.7), “special case”; SGA 4½ Etat 0 (1.2.1).
- [`CochainComplex.instHasShiftInt`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CochainComplex.instHasShiftInt#doc) registered with `add_to_stacks` in [StacksCore/Algebra/Homology/HomotopyCategory/Shift.lean, line 38](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Algebra/Homology/HomotopyCategory/Shift.lean#L38) (StacksCore): “the `HasShift` instance, which is what makes the notation `A⟦k⟧` available and packages the shifts of all `k` together.”. References: SGA 2 XIV (2.3).
- [`CochainComplex.shiftFunctor_obj_X`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CochainComplex.shiftFunctor_obj_X#doc) registered with `add_to_stacks` in [StacksCore/Algebra/Homology/HomotopyCategory/Shift.lean, line 42](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Algebra/Homology/HomotopyCategory/Shift.lean#L42) (StacksCore): “clause 1: `A[k]^n = A^{n+k}`, on the nose.”. References: SGA 4 XVII (1.1.4.2.1), “special case”.
- [`CochainComplex.shiftFunctor_obj_d`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CochainComplex.shiftFunctor_obj_d#doc) registered with `add_to_stacks` in [StacksCore/Algebra/Homology/HomotopyCategory/Shift.lean, line 45](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Algebra/Homology/HomotopyCategory/Shift.lean#L45) (StacksCore): “clause 2: `d_{A[k]}^n = (-1)^k d_A^{n+k}`, where the sign is `Int.negOnePow k` in `ℤˣ` because `(-1 : ℤ)^k` does not exist for negative `k`. It depends on `k` and not on `n`, as in the Stacks project.”. References: SGA 4 XVII (1.1.4.2.1), “special case”; SGA 4 XVII (2.2.7), “partial”.
- [`CochainComplex.shiftFunctor_map_f`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CochainComplex.shiftFunctor_map_f#doc) registered with `add_to_stacks` in [StacksCore/Algebra/Homology/HomotopyCategory/Shift.lean, line 50](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Algebra/Homology/HomotopyCategory/Shift.lean#L50) (StacksCore): “the last sentence, `f[k]^n = f^{k+n}`; Mathlib writes the index as `n + k`, which is the same integer but not the same term, so the two spellings have different syntactic types.”.

## Tag 011H, a definition

[Tag 011H](https://stacks.math.columbia.edu/tag/011H) in the Stacks Project.

Declarations registered for the tag:

- [`CochainComplex.ShiftSequence.shiftIso`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CochainComplex.ShiftSequence.shiftIso#doc) registered with `add_to_stacks` in [StacksCore/Algebra/Homology/HomotopyCategory/ShiftSequence.lean, line 43](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Algebra/Homology/HomotopyCategory/ShiftSequence.lean#L43) (StacksCore): “the identification itself, as an isomorphism of functors; the Stacks arrow `H^{i+k}(A^•) → H^i(A[k]^•)` is its `.inv` component.”.
- [`CochainComplex.ShiftSequence.shiftIso_hom_app`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CochainComplex.ShiftSequence.shiftIso_hom_app#doc) registered with `add_to_stacks` in [StacksCore/Algebra/Homology/HomotopyCategory/ShiftSequence.lean, line 47](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Algebra/Homology/HomotopyCategory/ShiftSequence.lean#L47) (StacksCore): “that the identification really is the plain re-indexing: it is the map induced on homology by an isomorphism of short complexes whose middle component is unsigned.”.

## Tag 011I, a lemma

[Tag 011I](https://stacks.math.columbia.edu/tag/011I) in the Stacks Project.

**`Homotopy.equivHomShift`**, a def in StacksCore (human-reviewed), declared in [StacksCore/Algebra/Homology/HomotopyCategory/HomComplexShift.lean, line 46](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Algebra/Homology/HomotopyCategory/HomComplexShift.lean#L46).

> **Stacks 011I**, second sentence. Given one homotopy `h₀` from `a` to `b`, the homotopies from
> `a` to `b` correspond to the morphisms of complexes `A^• ⟶ B[-1]^•`, by `h ↦ h - h₀`. Together
> with the fact that the target is a group, this is the assertion that the homotopies from `a` to
> `b` form a principal homogeneous space under it whenever they are nonempty.

```lean
noncomputable def equivHomShift (h₀ : Homotopy a b) : Homotopy a b ≃ (A ⟶ B⟦(-1 : ℤ)⟧)
```

## Tag 011J, a lemma

[Tag 011J](https://stacks.math.columbia.edu/tag/011J) in the Stacks Project.

Declarations registered for the tag:

- [`CochainComplex.homOfDegreewiseSplit`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CochainComplex.homOfDegreewiseSplit#doc) registered with `add_to_stacks` in [StacksCore/Algebra/Homology/HomotopyCategory/DegreewiseSplit.lean, line 51](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Algebra/Homology/HomotopyCategory/DegreewiseSplit.lean#L51) (StacksCore): “the morphism `δ : C^• → A[1]^•` itself.”.
- [`CochainComplex.homOfDegreewiseSplit_f`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CochainComplex.homOfDegreewiseSplit_f#doc) registered with `add_to_stacks` in [StacksCore/Algebra/Homology/HomotopyCategory/DegreewiseSplit.lean, line 54](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Algebra/Homology/HomotopyCategory/DegreewiseSplit.lean#L54) (StacksCore): “its components, `δ^n = π^{n+1} ∘ d_B^n ∘ s^n` read in diagrammatic order.”.

## Tag 011K, a lemma

[Tag 011K](https://stacks.math.columbia.edu/tag/011K) in the Stacks Project.

**`CochainComplex.homologyMap_homOfDegreewiseSplit`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/Algebra/Homology/HomotopyCategory/DegreewiseSplit.lean, line 202](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Algebra/Homology/HomotopyCategory/DegreewiseSplit.lean#L202).

> **Stacks 011K.** The morphism `δ : C^• → A[1]^•` attached to a degreewise split short exact
> sequence induces on cohomology exactly the connecting map of the long exact sequence of 0117,
> under the identification `H^i(A[1]^•) = H^{i+1}(A^•)` of tag 011H.
>
> The proof is a diagram chase on the tautological cycle: `δ_eq` computes the connecting map from
> any lift of a cycle of `C^•` along `B^• → C^•`, the splitting provides that lift as `(σ i).s`, and
> `liftCycles_shift_homologyπ` moves the result across the shift identification.

```lean
theorem homologyMap_homOfDegreewiseSplit (S : ShortComplex (CochainComplex C ℤ))
    (σ : ∀ n, (S.map (eval C (up ℤ) n)).Splitting) (hS : S.ShortExact)
    (i j : ℤ) (hij : (up ℤ).Rel i j) (h : 1 + i = j) :
    HomologicalComplex.homologyMap (homOfDegreewiseSplit S σ) i ≫
        ((homologyFunctor C (up ℤ) 0).shiftIso 1 i j h).hom.app S.X₁ =
      hS.δ i j hij
```

**`main_theorem_delta_eq_connecting`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DGA/AdmissibleSequenceConnectingMap.lean, line 240](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DGA/AdmissibleSequenceConnectingMap.lean#L240). The attribute's comment: “the homology map read through the inverse of the shift identification”.

> For a short exact sequence `E.S` split in each degree, the map induced on `n`-th cohomology
> by the morphism `CochainComplex.homOfDegreewiseSplit E.S E.σ : C ⟶ A⟦1⟧` is the connecting
> homomorphism `hS.δ n (n + 1) rfl : H^n(C) → H^{n+1}(A)` followed by the inverse of the shift
> isomorphism `H^n(A⟦1⟧) ≅ H^{n+1}(A)`.

```lean
theorem main_theorem_delta_eq_connecting
    (C : Type*) [Category C] [Abelian C]
    (E : AdmissibleSES C)
    (hS : E.S.ShortExact) (n : ℤ) :
    HomologicalComplex.homologyMap (CochainComplex.homOfDegreewiseSplit E.S E.σ) n =
      hS.δ n (n + 1) rfl ≫
        ((CochainComplex.ShiftSequence.shiftIso C 1 n (n + 1) (by ring)).app E.S.X₁).inv
```

## Tag 011L, a lemma

[Tag 011L](https://stacks.math.columbia.edu/tag/011L) in the Stacks Project.

**`CochainComplex.retractionSubHom_eq_neg`**, a lemma in StacksCore (human-reviewed), declared in [StacksCore/Algebra/Homology/HomotopyCategory/DegreewiseSplit.lean, line 113](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Algebra/Homology/HomotopyCategory/DegreewiseSplit.lean#L113). The attribute's comment: “(1)”.

> **Stacks 011L**, part (1): `gⁿ = -hⁿ`.

```lean
lemma retractionSubHom_eq_neg (n : ℤ) : retractionSubHom S σ σ' n = -sectionSubHom S σ σ' n
```

**`CochainComplex.homotopyHomOfDegreewiseSplit`**, a def in StacksCore (human-reviewed), declared in [StacksCore/Algebra/Homology/HomotopyCategory/DegreewiseSplit.lean, line 163](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Algebra/Homology/HomotopyCategory/DegreewiseSplit.lean#L163). The attribute's comment: “(2)”.

> **Stacks 011L**, part (2): the family `gⁿ` is a homotopy between the two connecting morphisms
> `δ, δ' : C^• ⟶ A[1]^•` of tag 011J.
>
> Part (1) is what makes this true with `g` rather than `h`: passing a `0`-cochain `C^• ⟶ A^•` to a
> `(-1)`-cochain `C^• ⟶ A[1]^•` conjugates `δ` by `Cochain.δ_rightShift`'s `(-1)^1`, and that sign
> is exactly the one relating `g` to `h`.

```lean
noncomputable def homotopyHomOfDegreewiseSplit :
    Homotopy (homOfDegreewiseSplit S σ') (homOfDegreewiseSplit S σ)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 12.14, Tag 0119](https://stacks.math.columbia.edu/tag/0119)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
