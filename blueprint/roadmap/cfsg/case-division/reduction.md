---
declaration: theorem
origin: cited
lean: CFSG.Assembly.GroupProp, CFSG.Assembly.KProper, CFSG.Assembly.OddOrderStatement, CFSG.Assembly.AbelianStatement, CFSG.Assembly.DisconnectedStatement, CFSG.Assembly.LowTwoRankStatement, CFSG.Assembly.DichotomyStatement, CFSG.Assembly.ComponentStatement, CFSG.Assembly.QuasithinStatement, CFSG.Assembly.RankThreeStatement, CFSG.Assembly.LargeEvenStatement, CFSG.Assembly.charTwo_classification, CFSG.Assembly.kProper_classification, CFSG.Assembly.classification
statement: formalized
proof: formalized
---

# CFSG.Assembly.Reduction

The module `CFSG.Assembly.Reduction` defines each case of the proof's case division as a proposition and derives the classification from them. Its 14 declarations, in file order, quoted from [CFSG/Assembly/Reduction.lean](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Assembly/Reduction.lean) in [AxiomMath/CFSG](https://github.com/AxiomMath/CFSG) at commit [69cb972f](https://github.com/AxiomMath/CFSG/tree/69cb972f587a3ecc035e092253167ff2e303c962), Apache-2.0; each definition is shown whole:

`CFSG.Assembly.GroupProp` (abbrev, [line 10](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Assembly/Reduction.lean#L10)). A definition.

```lean
abbrev GroupProp : Type 1 := ∀ (G : Type) [Group G], Prop
```

`CFSG.Assembly.KProper` (def, [line 14](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Assembly/Reduction.lean#L14)). A definition.

```lean
@[expose] def KProper (G : Type) [Group G] : Prop := KCore.KProperNonab C G
```

`CFSG.Assembly.OddOrderStatement` (def, [line 16](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Assembly/Reduction.lean#L16)). A definition.

```lean
@[expose] def OddOrderStatement : Prop :=
  ∀ (G : Type) [Group G] [Finite G], Odd (Nat.card G) → Group.IsSolvable G
```

`CFSG.Assembly.AbelianStatement` (def, [line 19](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Assembly/Reduction.lean#L19)). A definition.

```lean
@[expose] def AbelianStatement : Prop :=
  ∀ (G : Type) [Group G] [Finite G] [IsSimpleGroup G], (∀ a b : G, a * b = b * a) → C G
```

`CFSG.Assembly.DisconnectedStatement` (def, [line 22](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Assembly/Reduction.lean#L22)). A definition.

```lean
@[expose] def DisconnectedStatement : Prop :=
  ∀ (G : Type) [Group G] [Finite G] [IsSimpleGroup G], (∃ a b : G, a * b ≠ b * a) →
    Even (Nat.card G) → ¬ (involutionGraph G).Preconnected → C G
```

`CFSG.Assembly.LowTwoRankStatement` (def, [line 26](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Assembly/Reduction.lean#L26)). A definition.

```lean
@[expose] def LowTwoRankStatement : Prop :=
  ∀ (G : Type) [Group G] [Finite G] [IsSimpleGroup G], (∃ a b : G, a * b ≠ b * a) →
    Even (Nat.card G) → twoRank G ≤ 2 → C G
```

`CFSG.Assembly.DichotomyStatement` (def, [line 30](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Assembly/Reduction.lean#L30)). A definition.

```lean
@[expose] def DichotomyStatement : Prop :=
  ∀ (G : Type) [Group G] [Finite G] [IsSimpleGroup G], (∃ a b : G, a * b ≠ b * a) →
    3 ≤ twoRank G → (involutionGraph G).Connected → IsComponentType G ∨ IsCharTwoType G
```

`CFSG.Assembly.ComponentStatement` (def, [line 34](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Assembly/Reduction.lean#L34)). A definition.

```lean
@[expose] def ComponentStatement : Prop :=
  ∀ (G : Type) [Group G] [Finite G] [IsSimpleGroup G], (∃ a b : G, a * b ≠ b * a) →
    KProper C G → 3 ≤ twoRank G → IsComponentType G → C G
```

`CFSG.Assembly.QuasithinStatement` (def, [line 38](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Assembly/Reduction.lean#L38)). A definition.

```lean
@[expose] def QuasithinStatement : Prop :=
  ∀ (G : Type) [Group G] [Finite G] [IsSimpleGroup G], (∃ a b : G, a * b ≠ b * a) →
    KProper C G → IsCharTwoType G → evenRank G ≤ 2 → C G
```

`CFSG.Assembly.RankThreeStatement` (def, [line 42](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Assembly/Reduction.lean#L42)). A definition.

```lean
@[expose] def RankThreeStatement : Prop :=
  ∀ (G : Type) [Group G] [Finite G] [IsSimpleGroup G], (∃ a b : G, a * b ≠ b * a) →
    KProper C G → IsCharTwoType G → evenRank G = 3 → C G
```

`CFSG.Assembly.LargeEvenStatement` (def, [line 46](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Assembly/Reduction.lean#L46)). A definition.

```lean
@[expose] def LargeEvenStatement : Prop :=
  ∀ (G : Type) [Group G] [Finite G] [IsSimpleGroup G], (∃ a b : G, a * b ≠ b * a) →
    KProper C G → IsCharTwoType G → 4 ≤ evenRank G → C G
```

`CFSG.Assembly.charTwo_classification` (theorem, [line 50](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Assembly/Reduction.lean#L50)). Proved here.

```lean
theorem charTwo_classification (hqt : QuasithinStatement C) (hr3 : RankThreeStatement C)
    (hle : LargeEvenStatement C) (G : Type) [Group G] [Finite G] [IsSimpleGroup G]
    (hnonab : ∃ a b : G, a * b ≠ b * a) (hK : KProper C G) (hchar : IsCharTwoType G) : C G
```

`CFSG.Assembly.kProper_classification` (theorem, [line 58](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Assembly/Reduction.lean#L58)). Proved here.

```lean
theorem kProper_classification (hodd : OddOrderStatement) (hab : AbelianStatement C)
    (hdisc : DisconnectedStatement C) (hlow : LowTwoRankStatement C) (hdich : DichotomyStatement)
    (hcomp : ComponentStatement C) (hqt : QuasithinStatement C) (hr3 : RankThreeStatement C)
    (hle : LargeEvenStatement C) (G : Type) [Group G] [Finite G] [IsSimpleGroup G]
    (hK : KProper C G) : C G
```

`CFSG.Assembly.classification` (theorem, [line 81](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Assembly/Reduction.lean#L81)). Proved here.

```lean
theorem classification (hodd : OddOrderStatement) (hab : AbelianStatement C)
    (hdisc : DisconnectedStatement C) (hlow : LowTwoRankStatement C) (hdich : DichotomyStatement)
    (hcomp : ComponentStatement C) (hqt : QuasithinStatement C) (hr3 : RankThreeStatement C)
    (hle : LargeEvenStatement C) (G : Type) [Group G] [Finite G] [IsSimpleGroup G] : C G
```

## Depends on

It uses no other result mapped here.

## Sources

- [CFSG/Assembly/Reduction.lean at 69cb972f](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Assembly/Reduction.lean)
