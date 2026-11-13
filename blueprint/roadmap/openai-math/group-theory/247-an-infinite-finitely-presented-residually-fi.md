---
declaration: section
origin: cited
lean: OAI.SourceBurnside.thm_main
statement: formalized
proof: formalized
---

# 247. An infinite finitely presented residually finite 2-group and a finitely presented nil algebra

2 manuscripts and 1 Lean statement, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Constructs an infinite finitely presented residually finite group whose elements all have finite 2-power order, answering the finitely presented Burnside problem negatively even in this class. The construction also yields an infinite-dimensional finitely presented nil associative 𝔽$_{2}$-algebra and a finitely presented infinite-dimensional algebraic unitization, giving negative answers to the corresponding nilpotence and Kurosh finiteness questions.

## An infinite finitely presented residually finite 2-group

We prove that the infinite, ordinarily finitely presented periodic Steinberg group $\Gamma=\mathop{\mathrm{St}}\nolimits _{12}(R)$ of a companion paper is residually finite. Its finite-index subgroup $G=\ker(\Gamma\to\mathop{\mathrm{St}}\nolimits _{12}(\mathbb F_2))$ is infinite, ordinarily finitely presented, and residually finite, and every element of *G* has finite 2-power order. The orders of its elements are unbounded. Phases of long words in the companion's graded algebra allow finite degree truncations to detect all elements of Γ, including the central kernel.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/An-infinite-finitely-presented-residually-finite-2-group-October-5-2026/residually-finite-torsion.pdf).

## An infinite finitely presented periodic group

We construct an infinite group with an ordinary finite presentation in which every element has finite order, answering the finitely presented Burnside question negatively. We also construct an infinite-dimensional finitely presented nonunital nil associative algebra over 𝔽$_{2}$ that is Jacobson radical but not nilpotent. Its unitization is finitely presented, algebraic, and infinite-dimensional. These algebras answer the finitely presented nil- and radical-algebra nilpotence questions and the finite-presentation version of Kurosh's algebraic finiteness question negatively.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/An-infinite-finitely-presented-periodic-group-September-23-2026/paper.pdf); the Lean below formalizes results from it.

## The Lean formalization

The finitely presented Burnside question asks whether a finitely presented group in which every element has finite order must be finite. The formalization gives a negative answer by constructing an infinite finitely presented periodic group, including a witness realized as a Steinberg group over an algebra of characteristic two. Periodicity means that each element has some finite order; no common exponent is asserted. The paper's separate nil-algebra and radical-algebra conclusions are outside these selected statements.

## Lean: Infinite finitely presented periodic group

```lean
theorem thm_main : MainStatement ∧ BurnsideStatement
```

Stated in [PeriodicGroup.lean, line 51](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/PeriodicGroup.lean#L51). Proved in [lean/OAI/GroupTheory/PeriodicGroups/Main.lean, line 18](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/GroupTheory/PeriodicGroups/Main.lean#L18).

## Depends on

No dependencies are recorded here: the chapter draws no edges between families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/247.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/247.md)
