---
catalog: module
lean: AlgebraTower, AlgebraTower.ofNatStep, AlgebraTower.ofNatStep_algebraMap_succ_right, AlgebraTower.ofNatStep_algebraMap_succ, AlgebraTower.algebraMap_self, AlgebraTower.algebraMap_self_apply, AlgebraTower.toAlgebra, AlgebraTower.toIsScalarTower, AlgebraTowerEquiv, AlgebraTowerEquiv.commutesRight', AlgebraTowerEquiv.symm, AlgebraTowerEquiv.algebraMapRightUp, AlgebraTowerEquiv.algebraMapLeftUp, AlgebraTowerEquiv.toAlgebraOverLeft, AlgebraTowerEquiv.toAlgebraOverRight, AlgebraTowerEquiv.toAlgEquivOverLeft, AlgebraTowerEquiv.toAlgEquivOverRight
statement: formalized
proof: formalized
---

# Towers of algebras and their equivalences

`CompPoly.Data.RingTheory.AlgebraTower`, in [CompPoly/Data/RingTheory/AlgebraTower.lean](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Data/RingTheory/AlgebraTower.lean), by Chung Thai Nguyen, Quang Dao.

> An `AlgebraTower` is a preorder-indexed family of commutative semirings with ring
> homomorphisms between comparable levels. Self-maps are identities, and the maps compose
> along chains of indices. Each map induces an algebra structure on its target, and
> composition gives compatible scalar actions across three levels.
>
> `AlgebraTower.ofNatStep` constructs a natural-number-indexed tower by composing chosen
> homomorphisms between adjacent levels. These homomorphisms need not be injective.
>
> An `AlgebraTowerEquiv` consists of ring equivalences at each level that commute with
> the tower maps.

`AlgebraTower` (class, [line 32](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Data/RingTheory/AlgebraTower.lean#L32))

> A preorder-indexed family of commutative semirings with compatible ring homomorphisms.
>
> The map from a level to itself is the identity. For `i ≤ j ≤ k`, the map from `i` to `k`
> is the composite of the maps from `i` to `j` and from `j` to `k`.

```lean
class AlgebraTower {ι : Type*} [Preorder ι] (AT : ι → Type*)
  [∀ i, CommSemiring (AT i)] where
  /-- Ring homomorphisms from `AT i` to `AT j` for all `i ≤ j`. -/
  protected algebraMap : ∀ i j, (h : i ≤ j) → (AT i →+* AT j)
  /-- The ring homomorphism from level `i` to itself is the identity. -/
  algebraMap_self' : ∀ i, algebraMap i i le_rfl = RingHom.id (AT i)
  /-- Every image element commutes with every element of the target semiring. -/
  commutes' : ∀ (i j : ι) (h : i ≤ j) (r : AT i) (x : AT j),
    (algebraMap i j h r) * x = x * (algebraMap i j h r)
  /-- The map from `i` to `k` is the composite of the maps from `i` to `j` and `j` to `k`. -/
  coherence' : ∀ (i j k : ι) (h1 : i ≤ j) (h2 : j ≤ k),
    algebraMap i k (h1.trans h2) =
      (algebraMap j k h2).comp (algebraMap i j h1)
```

`AlgebraTower.ofNatStep` (definition, [line 57](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Data/RingTheory/AlgebraTower.lean#L57))

> Construct a tower by composing chosen ring homomorphisms between adjacent levels.
>
> The map from a level to itself is the identity. The map from `i` to `j + 1`, for `i ≤ j`,
> is `step j` composed with the map from `i` to `j`. No injectivity assumption is required.

```lean
def ofNatStep (step : ∀ k, A k →+* A (k + 1)) : AlgebraTower A
```

`AlgebraTower.ofNatStep_algebraMap_succ_right` (theorem, [line 70](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Data/RingTheory/AlgebraTower.lean#L70))

> Extending a constructed tower map by one level composes it with the chosen next map.

```lean
theorem ofNatStep_algebraMap_succ_right (step : ∀ k, A k →+* A (k + 1))
    {i j : ℕ} (h : i ≤ j) :
    (ofNatStep step).algebraMap i (j + 1) (h.trans (Nat.le_succ j)) =
      (step j).comp ((ofNatStep step).algebraMap i j h)
```

`AlgebraTower.ofNatStep_algebraMap_succ` (theorem, [line 78](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Data/RingTheory/AlgebraTower.lean#L78))

> The map between adjacent levels is the homomorphism supplied to the constructor.

```lean
theorem ofNatStep_algebraMap_succ (step : ∀ k, A k →+* A (k + 1))
    (i : ℕ) (h : i ≤ i + 1) :
    (ofNatStep step).algebraMap i (i + 1) h = step i
```

`AlgebraTower.algebraMap_self` (lemma, [line 95](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Data/RingTheory/AlgebraTower.lean#L95))

> The tower map from level `i` to itself is the identity for every proof of `i ≤ i`.

```lean
lemma AlgebraTower.algebraMap_self (i : ι) (h : i ≤ i) :
    AlgebraTower.algebraMap (AT := A) i i h = RingHom.id (A i)
```

`AlgebraTower.algebraMap_self_apply` (lemma, [line 100](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Data/RingTheory/AlgebraTower.lean#L100))

> The tower map from level `i` to itself fixes every element of that level.

```lean
lemma AlgebraTower.algebraMap_self_apply (i : ι) (h : i ≤ i) (x : A i) :
    AlgebraTower.algebraMap (AT := A) i i h x = x
```

`AlgebraTower.toAlgebra` (abbreviation, [line 105](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Data/RingTheory/AlgebraTower.lean#L105))

```lean
abbrev AlgebraTower.toAlgebra {i j : ι} (h : i ≤ j) : Algebra (A i) (A j)
```

`AlgebraTower.toIsScalarTower` (instance, [line 109](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Data/RingTheory/AlgebraTower.lean#L109))

```lean
instance AlgebraTower.toIsScalarTower (a : AlgebraTower C) {i j k : ι}
    (h1 : i ≤ j) (h2 : j ≤ k) :
    letI : Algebra (C i) (C j) := by exact a.toAlgebra h1
    letI : Algebra (C j) (C k) := by exact a.toAlgebra h2
    letI : Algebra (C i) (C k) := by exact a.toAlgebra (h1.trans h2)
    IsScalarTower (C i) (C j) (C k)
```

`AlgebraTowerEquiv` (structure, [line 130](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Data/RingTheory/AlgebraTower.lean#L130))

```lean
structure AlgebraTowerEquiv (A : ι → Type*) [∀ i, CommSemiring (A i)] [a : AlgebraTower A]
  (B : ι → Type*) [∀ i, CommSemiring (B i)] [b : AlgebraTower B]
  where
    toRingEquiv : ∀ i, (A i ≃+* B i)
    commutesLeft' : ∀ (i j : ι) (h : i ≤ j) (r : A i),
      (b.algebraMap (i:=i) (j:=j) (h:=h)) ((toRingEquiv i) r) =
      (toRingEquiv j) (a.algebraMap (i:=i) (j:=j) (h:=h) r)
```

`AlgebraTowerEquiv.commutesRight'` (lemma, [line 138](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Data/RingTheory/AlgebraTower.lean#L138))

```lean
lemma AlgebraTowerEquiv.commutesRight' (e : AlgebraTowerEquiv A B)
    {i j : ι} (h : i ≤ j) (r : B i) :
  AlgebraTower.algebraMap (AT:=A) (i:=i) (j:=j) (h:=h) ((e.toRingEquiv i).symm r) =
  (e.toRingEquiv j).symm (AlgebraTower.algebraMap (AT:=B) (i:=i) (j:=j) (h:=h) r)
```

`AlgebraTowerEquiv.symm` (definition, [line 149](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Data/RingTheory/AlgebraTower.lean#L149))

```lean
def AlgebraTowerEquiv.symm (e : AlgebraTowerEquiv A B) : AlgebraTowerEquiv B A
```

`AlgebraTowerEquiv.algebraMapRightUp` (definition, [line 153](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Data/RingTheory/AlgebraTower.lean#L153))

```lean
def AlgebraTowerEquiv.algebraMapRightUp (e : AlgebraTowerEquiv A B) (i j : ι)
    (h : i ≤ j) : (A i) →+* (B j)
```

`AlgebraTowerEquiv.algebraMapLeftUp` (definition, [line 159](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Data/RingTheory/AlgebraTower.lean#L159))

```lean
def AlgebraTowerEquiv.algebraMapLeftUp (e : AlgebraTowerEquiv A B) (i j : ι)
    (h : i ≤ j) : (B i) →+* (A j)
```

`AlgebraTowerEquiv.toAlgebraOverLeft` (abbreviation, [line 165](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Data/RingTheory/AlgebraTower.lean#L165))

```lean
abbrev AlgebraTowerEquiv.toAlgebraOverLeft (e : AlgebraTowerEquiv A B) (i j : ι)
    (h : i ≤ j) : Algebra (A i) (B j)
```

`AlgebraTowerEquiv.toAlgebraOverRight` (abbreviation, [line 169](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Data/RingTheory/AlgebraTower.lean#L169))

```lean
abbrev AlgebraTowerEquiv.toAlgebraOverRight (e : AlgebraTowerEquiv A B) (i j : ι)
    (h : i ≤ j) : Algebra (B i) (A j)
```

`AlgebraTowerEquiv.toAlgEquivOverLeft` (definition, [line 173](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Data/RingTheory/AlgebraTower.lean#L173))

```lean
def AlgebraTowerEquiv.toAlgEquivOverLeft (e : AlgebraTowerEquiv A B) (i j : ι) (h : i ≤ j) :
    letI : Algebra (A i) (A j) := by exact AlgebraTower.toAlgebra h
    letI : Algebra (A i) (B j) := by exact e.toAlgebraOverLeft i j h
    AlgEquiv (A i) (A j) (B j)
```

`AlgebraTowerEquiv.toAlgEquivOverRight` (definition, [line 196](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Data/RingTheory/AlgebraTower.lean#L196))

```lean
def AlgebraTowerEquiv.toAlgEquivOverRight (e : AlgebraTowerEquiv A B) (i j : ι) (h : i ≤ j) :
    letI : Algebra (B i) (B j) := by exact AlgebraTower.toAlgebra h
    letI : Algebra (B i) (A j) := by exact e.toAlgebraOverRight i j h
    AlgEquiv (B i) (B j) (A j)
```

## Depends on

Its statements use no other CompPoly module's declarations.

## Sources

- [CompPoly/Data/RingTheory/AlgebraTower.lean at c72a7652](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Data/RingTheory/AlgebraTower.lean)
- [Declaration ledger](../../../../sources/comppoly/CompPoly.Data.RingTheory.AlgebraTower.json)
