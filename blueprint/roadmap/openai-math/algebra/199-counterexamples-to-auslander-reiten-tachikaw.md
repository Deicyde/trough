---
declaration: section
origin: cited
lean: OAI.ArExplicit.Statement.main, OAI.Tachikawa.main_theorem
statement: formalized
proof: formalized
---

# 199. Counterexamples to Auslander–Reiten, Tachikawa and related homological conjectures

2 manuscripts and 2 Lean statements, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Constructs finite-dimensional algebras over a characteristic-two rational-function field that disprove the Auslander–Reiten and Gorenstein-projective conjectures, and Tachikawa's second conjecture. An associated endomorphism algebra also disproves the classical, generalized and strong Nakayama conjectures, the Auslander–Gorenstein conjecture, and the Wakamatsu tilting conjecture. The counterexamples persist under every extension of the base field.

## An explicit counterexample to the Auslander-Reiten conjecture

We disprove the Auslander–Reiten conjecture for Artin algebras. We construct a finite-dimensional algebra Λ over $k=\mathbb F_2(q,H_1,H_2)$ and a finite-dimensional nonprojective left module *Z* such that $\mathop{\mathrm{Ext}}\nolimits ^i_\Lambda(Z,Z)=\mathop{\mathrm{Ext}}\nolimits ^i_\Lambda(Z,\Lambda)=0$ for every *i* > 0. The module is Gorenstein-projective, so the same example also disproves the Gorenstein-projective conjecture. Both counterexamples persist after every extension of *k*.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/An-explicit-counterexample-to-the-Auslander-Reiten-conjecture-September-23-2026/paper.pdf); the Lean below formalizes results from it.

## A counterexample to Tachikawa's second conjecture

We disprove Tachikawa's second conjecture by constructing a finite-dimensional symmetric algebra over $k=\mathbb F_2(q,H_1,H_2)$ with a finite-dimensional nonprojective module whose self-extension groups vanish in every positive degree. The associated endomorphism algebra also gives counterexamples to the classical, generalized, and strong Nakayama conjectures, the Auslander–Gorenstein conjecture, and the Wakamatsu tilting conjecture. These conclusions persist after every extension of *k*.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/A-counterexample-to-Tachikawas-second-conjecture-September-23-2026/paper.pdf); the Lean below formalizes results from it.

## The Lean formalization

The Auslander–Reiten conjecture predicts that a finitely generated module $M$ over an Artin algebra $A$ is projective if $\mathrm{Ext}^i_A(M,M\oplus A)=0$ for every $i>0$. The formalized counterexample is a finite-dimensional algebra over $k=\mathbb F_2(q,H_1,H_2)$ and a finite-dimensional nonprojective Gorenstein-projective module with this vanishing.

It also establishes $A/\mathrm{rad}\,A\cong k^8$, $(\mathrm{rad}\,A)^4\ne0$, and preservation of the listed properties after every field extension. The Tachikawa companion is separate.

Tachikawa's second conjecture predicts that a finite-dimensional module over a finite-dimensional self-injective algebra is projective if all its positive-degree self-Ext groups vanish. The formalized counterexample gives a finite-dimensional symmetric algebra over $\mathbb F_2(q,H_1,H_2)$ and a finite-dimensional nonprojective module $M$ with $\mathrm{Ext}^i(M,M)=0$ for every $i>0$. Symmetric algebras are self-injective, so this contradicts the conjecture.

The later field-extension, endomorphism-algebra, and related homological consequences are not included.

## Lean: Auslander–Reiten counterexample

```lean
theorem main : FullStatement.{v}
```

Stated in [AuslanderReiten.lean, line 70](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/AuslanderReiten.lean#L70). Proved in [lean/OAI/Algebra/AuslanderReiten/All.lean, line 738](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Algebra/AuslanderReiten/All.lean#L738). formalization.yaml lists it as one of the repository's main results.

## Lean: Tachikawa counterexample

```lean
theorem main_theorem : Counterexample
```

Stated in [Tachikawa.lean, line 32](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/Tachikawa.lean#L32). Proved in [lean/OAI/RingTheory/Tachikawa/Counterexample.lean, line 293](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/RingTheory/Tachikawa/Counterexample.lean#L293). formalization.yaml lists it as one of the repository's main results.

## Depends on

No dependencies are recorded here: the chapter draws no edges between families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/199.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/199.md)
