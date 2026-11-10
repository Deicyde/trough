---
declaration: theorem
origin: cited
lean: CFSG.Milestones.cl_lit_fischer_three_transposition_theorem, CFSG.Milestones.cl_lit_fischer_three_transposition_theorem_pinned, CFSG.Milestones.cl_lit_fischer_three_transposition_theorem_recognition
statement: formalized
proof: formalized
---

# CL_LIT_Fischer_three_transposition_theorem

The milestone module `CFSG.Milestones.CL_LIT_Fischer_three_transposition_theorem`, one of those CFSG/Milestones.lean imports.

It declares 3 results, quoted from [CFSG/Milestones/CL_LIT_Fischer_three_transposition_theorem.lean](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CL_LIT_Fischer_three_transposition_theorem.lean) in [AxiomMath/CFSG](https://github.com/AxiomMath/CFSG) at commit [69cb972f](https://github.com/AxiomMath/CFSG/tree/69cb972f587a3ecc035e092253167ff2e303c962), Apache-2.0:

`CFSG.Milestones.cl_lit_fischer_three_transposition_theorem` (theorem, [line 15](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CL_LIT_Fischer_three_transposition_theorem.lean#L15)). Proved here.

```lean
theorem _root_.CFSG.Milestones.cl_lit_fischer_three_transposition_theorem
    (G : Type) [Group G] [Finite G] (D : Set G)
    (hclass : ∃ d₀ : G, D = {g | IsConj d₀ g})
    (hinv : ∀ d ∈ D, orderOf d = 2)
    (hprod : ∀ d ∈ D, ∀ e ∈ D, orderOf (d * e) ∈ ({1, 2, 3} : Set ℕ))
    (hgen : Subgroup.closure D = ⊤)
    (hcenter : Subgroup.center G = ⊥)
    (hsimple : IsSimpleGroup (commutator G)) :
    (∃ m : ℕ, (m = 3 ∨ 5 ≤ m) ∧
      ∃ φ : G ≃* Equiv.Perm (Fin m), ∀ g : G, g ∈ D ↔ (φ g).IsSwap) ∨
    (∃ m : ℕ, 2 ≤ m ∧ ∃ b : LinearMap.BilinForm (ZMod 2) (Fin (2 * m) → ZMod 2),
      (∀ x, b x x = 0) ∧ (∀ x, (∀ y, b x y = 0) → x = 0) ∧
      fischerLinearModel D
        (fischerMatrixGroup fun A => ∀ x y, b (A *ᵥ x) (A *ᵥ y) = b x y)
        (fischerTransvections (fun x y => b x y) fun v => v ≠ 0)) ∨
    (∃ m : ℕ, 2 ≤ m ∧ ∃ Q : QuadraticForm (ZMod 2) (Fin (2 * m) → ZMod 2),
      (∀ x, (∀ y, QuadraticMap.polar Q x y = 0) → x = 0) ∧
      (m = 2 → ¬ ∃ W : Submodule (ZMod 2) (Fin (2 * m) → ZMod 2),
        Module.finrank (ZMod 2) W = 2 ∧ ∀ w ∈ W, Q w = 0) ∧
      fischerLinearModel D
        (fischerMatrixGroup fun A => ∀ x, Q (A *ᵥ x) = Q x)
        (fischerTransvections (QuadraticMap.polar Q) fun v => Q v = 1)) ∨
    (∃ m : ℕ, 4 ≤ m ∧
      fischerCentralQuotientModel D
        (fischerMatrixGroup fun A => A.det = 1 ∧
          ∀ x y, fischerHermitianF4 m (A *ᵥ x) (A *ᵥ y) = fischerHermitianF4 m x y)
        (fischerTransvections (fischerHermitianF4 m)
          fun v => v ≠ 0 ∧ fischerHermitianF4 m v v = 0)) ∨
    (∃ m : ℕ, 5 ≤ m ∧ ∃ f : LinearMap.BilinForm (ZMod 3) (Fin m → ZMod 3),
      (∀ x y, f x y = f y x) ∧ (∀ x, (∀ y, f x y = 0) → x = 0) ∧
      fischerCentralQuotientModel D
        (Subgroup.closure (fischerTransvections (fun x y => f x y) fun v => f v v = 1))
        (fischerTransvections (fun x y => f x y) fun v => f v v = 1)) ∨
    (Nat.card G = 2 ^ 17 * 3 ^ 9 * 5 ^ 2 * 7 * 11 * 13 ∧ Nat.card D = 3510) ∨
    (Nat.card G = 2 ^ 18 * 3 ^ 13 * 5 ^ 2 * 7 * 11 * 13 * 17 * 23 ∧ Nat.card D = 31671) ∨
    (Nat.card G = 2 ^ 22 * 3 ^ 16 * 5 ^ 2 * 7 ^ 3 * 11 * 13 * 17 * 23 * 29 ∧
      Nat.card D = 306936)
```

`CFSG.Milestones.cl_lit_fischer_three_transposition_theorem_pinned` (theorem, [line 59](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CL_LIT_Fischer_three_transposition_theorem.lean#L59)). Proved here.

```lean
theorem _root_.CFSG.Milestones.cl_lit_fischer_three_transposition_theorem_pinned
    (G : Type) [Group G] [Finite G] (D : Set G)
    (hclass : ∃ d₀ : G, D = {g | IsConj d₀ g})
    (hinv : ∀ d ∈ D, orderOf d = 2)
    (hprod : ∀ d ∈ D, ∀ e ∈ D, orderOf (d * e) ∈ ({1, 2, 3} : Set ℕ))
    (hgen : Subgroup.closure D = ⊤)
    (hcenter : Subgroup.center G = ⊥)
    (hsimple : IsSimpleGroup (commutator G)) :
    (∃ m : ℕ, (m = 3 ∨ 5 ≤ m) ∧
      ∃ φ : G ≃* Equiv.Perm (Fin m), ∀ g : G, g ∈ D ↔ (φ g).IsSwap) ∨
    (∃ m : ℕ, 2 ≤ m ∧ ∃ b : LinearMap.BilinForm (ZMod 2) (Fin (2 * m) → ZMod 2),
      (∀ x, b x x = 0) ∧ (∀ x, (∀ y, b x y = 0) → x = 0) ∧
      fischerLinearModel D
        (fischerMatrixGroup fun A => ∀ x y, b (A *ᵥ x) (A *ᵥ y) = b x y)
        (fischerTransvections (fun x y => b x y) fun v => v ≠ 0)) ∨
    (∃ m : ℕ, 2 ≤ m ∧ ∃ Q : QuadraticForm (ZMod 2) (Fin (2 * m) → ZMod 2),
      (∀ x, (∀ y, QuadraticMap.polar Q x y = 0) → x = 0) ∧
      (m = 2 → ¬ ∃ W : Submodule (ZMod 2) (Fin (2 * m) → ZMod 2),
        Module.finrank (ZMod 2) W = 2 ∧ ∀ w ∈ W, Q w = 0) ∧
      fischerLinearModel D
        (fischerMatrixGroup fun A => ∀ x, Q (A *ᵥ x) = Q x)
        (fischerTransvections (QuadraticMap.polar Q) fun v => Q v = 1)) ∨
    (∃ m : ℕ, 4 ≤ m ∧
      fischerCentralQuotientModel D
        (fischerMatrixGroup fun A => A.det = 1 ∧
          ∀ x y, fischerHermitianF4 m (A *ᵥ x) (A *ᵥ y) = fischerHermitianF4 m x y)
        (fischerTransvections (fischerHermitianF4 m)
          fun v => v ≠ 0 ∧ fischerHermitianF4 m v v = 0)) ∨
    (∃ m : ℕ, 5 ≤ m ∧ ∃ f : LinearMap.BilinForm (ZMod 3) (Fin m → ZMod 3),
      (∀ x y, f x y = f y x) ∧ (∀ x, (∀ y, f x y = 0) → x = 0) ∧
      fischerCentralQuotientModel D
        (Subgroup.closure (fischerTransvections (fun x y => f x y) fun v => f v v = 1))
        (fischerTransvections (fun x y => f x y) fun v => f v v = 1)) ∨
    (∃ φ : G ≃* Blueprint.NativeSporadic.Fi22, Blueprint.Fischer.Pair _ (φ '' D) ∧
      ∀ E : Set Blueprint.NativeSporadic.Fi22, Blueprint.Fischer.Pair _ E → E = φ '' D) ∨
    (∃ φ : G ≃* Blueprint.NativeSporadic.Fi23, Blueprint.Fischer.Pair _ (φ '' D) ∧
      ∀ E : Set Blueprint.NativeSporadic.Fi23, Blueprint.Fischer.Pair _ E → E = φ '' D) ∨
    (∃ φ : G ≃* MulAut Blueprint.NativeSporadic.Fi24prime, Blueprint.Fischer.Pair _ (φ '' D) ∧
      ∀ E : Set (MulAut Blueprint.NativeSporadic.Fi24prime),
        Blueprint.Fischer.Pair _ E → E = φ '' D)
```

`CFSG.Milestones.cl_lit_fischer_three_transposition_theorem_recognition` (theorem, [line 111](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CL_LIT_Fischer_three_transposition_theorem.lean#L111)). Proved here.

```lean
theorem _root_.CFSG.Milestones.cl_lit_fischer_three_transposition_theorem_recognition
    (G : Type) [Group G] [Finite G] (D : Set G)
    (hclass : ∃ d₀ : G, D = {g | IsConj d₀ g})
    (hinv : ∀ d ∈ D, orderOf d = 2)
    (hprod : ∀ d ∈ D, ∀ e ∈ D, orderOf (d * e) ∈ ({1, 2, 3} : Set ℕ))
    (hgen : Subgroup.closure D = ⊤)
    (hcenter : Subgroup.center G = ⊥)
    (hsimple : IsSimpleGroup (commutator G))
    (d : G) (hd : d ∈ D) :
    let C := Subgroup.centralizer ({d} : Set G)
    (Nonempty (G ≃* Blueprint.NativeSporadic.Fi22) ↔
      ∃ K : Subgroup G, IsComponentOf K C ∧
        Blueprint.LieModel (K ⧸ Subgroup.center K) .PSU 6 2 1) ∧
    (Nonempty (G ≃* Blueprint.NativeSporadic.Fi23) ↔
      ∃ K : Subgroup G, IsComponentOf K C ∧
        Nonempty ((K ⧸ Subgroup.center K) ≃* Blueprint.NativeSporadic.Fi22)) ∧
    (Nonempty (G ≃* MulAut Blueprint.NativeSporadic.Fi24prime) ↔
      ∃ K : Subgroup G, IsComponentOf K C ∧
        Nonempty ((K ⧸ Subgroup.center K) ≃* Blueprint.NativeSporadic.Fi23)) ∧
    (Nonempty (G ≃* Blueprint.NativeSporadic.Fi22) →
      commutator C = ⊤ ∧ (Subgroup.center C).map C.subtype = Subgroup.zpowers d ∧
        Nat.card (Subgroup.center C) = 2 ∧
        Blueprint.LieModel (C ⧸ Subgroup.center C) .PSU 6 2 1) ∧
    (Nonempty (G ≃* Blueprint.NativeSporadic.Fi23) →
      commutator C = ⊤ ∧ (Subgroup.center C).map C.subtype = Subgroup.zpowers d ∧
        Nat.card (Subgroup.center C) = 2 ∧
        Nonempty ((C ⧸ Subgroup.center C) ≃* Blueprint.NativeSporadic.Fi22)) ∧
    (Nonempty (G ≃* MulAut Blueprint.NativeSporadic.Fi24prime) →
      ∃ K : Subgroup G, Nonempty (K ≃* Blueprint.NativeSporadic.Fi23) ∧
        C = Subgroup.zpowers d ⊔ K ∧ Subgroup.zpowers d ⊓ K = ⊥ ∧
        Subgroup.zpowers d ≤ Subgroup.centralizer (K : Set G))
```

The files of 4 case theorems import it, directly or through other files: [`CFSG.Assembly.component_type`](../../case-division/case-hcomp-componentstatement.md), [`CFSG.Assembly.quasithin`](../../case-division/case-hqt-quasithinstatement.md), [`CFSG.Assembly.rank_three_even`](../../case-division/case-hr3-rankthreestatement.md), [`CFSG.Assembly.large_even`](../../case-division/case-hle-largeevenstatement.md).

## Depends on

- [CFSG.FeitThompson.isSolvable_of_odd_natCard](../../case-division/case-hodd-oddorderstatement.md)
- [CL_LIT_Fischer_3T_existence_uniqueness](cl-lit-fischer-3t-existence-uniqueness.md)
- [FAM_classical_model_membership](../part-04/fam-classical-model-membership.md)

## Sources

- [CFSG/Milestones/CL_LIT_Fischer_three_transposition_theorem.lean at 69cb972f](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/CL_LIT_Fischer_three_transposition_theorem.lean)
