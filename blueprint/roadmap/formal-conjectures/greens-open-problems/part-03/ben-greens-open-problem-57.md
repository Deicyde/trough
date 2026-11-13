---
declaration: theorem
origin: cited
lean: Green57.green_57.variants.z3_functional, Green57.green_57.variants.z3, Green57.green_57
statement: formalized
---

# Ben Green's Open Problem 57

> *Reference:* [Ben Green's Open Problem 57](https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf#section.8)
>
> Let $G$ be a finite abelian group. Consider the space $\Phi(G)$ of all functions on $G$ which
> are "convex combinations" (in the sense of complex coefficients $c_i$ with
> $\sum |c_i| \le 1$) of functions of the form
>
> $$\phi(g) := \mathbb{E}_{x_1 + x_2 + x_3 = g} f_1(x_2, x_3) f_2(x_1, x_3) f_3(x_1, x_2)$$
>
> with $\|f_i\|_\infty \le 1$ (where $f_i : G \times G \to \mathbb{C}$).
>
> Let $\Phi'(G)$ be the space defined similarly, but with $f_3(x_1, x_2)$ required to be
> a function of $x_1 + x_2$. Do $\Phi(G)$ and $\Phi'(G)$ coincide?
>
> **Note:** The "convex combination" here uses complex coefficients whose absolute values sum to
> at most 1 (cf. personal communication with B. Green, April 2026). Since the base sets are
> balanced (closed under multiplication by unit complex numbers), this absolutely convex hull
> equals the real convex hull of the complex-valued base set.
>
> **Motivation:** $\Phi(G)$ is a 'generalised convolution algebra' as considered by
> Conlon–Fox–Zhao, whereas $\Phi'(G)$ consists of Tao's $\text{UAP}_2(G)$-functions.

*Quoted from [FormalConjectures/GreensOpenProblems/57.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/57.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 3 research or textbook statements: 3 solved.

## `Green57.green_57.variants.z3_functional`

Solved: stated here; a Lean proof is at [https://github.com/mo271/formal-conjectures/blob/f5afe85e1e02611f63c32ae041b33c67b7938cba/FormalConjectures/GreensOpenProblems/57.lean#L1071](https://github.com/mo271/formal-conjectures/blob/f5afe85e1e02611f63c32ae041b33c67b7938cba/FormalConjectures/GreensOpenProblems/57.lean#L1071).

> For $G = \mathbb{Z}/3\mathbb{Z}$ and the functional $a(0) = -1$, $a(1) = -3$, $a(2) = 3$,
> does the support function of $\Phi$ at $a$ strictly exceed that of $\Phi'$?
>
> Numerical evidence suggests the answer is **yes**:
>
> $$\sup_{\varphi \in \Phi'(\mathbb{Z}/3\mathbb{Z})} \operatorname{Re}\langle a, \varphi \rangle
>   \;\lt \; \sup_{\varphi \in \Phi(\mathbb{Z}/3\mathbb{Z})} \operatorname{Re}\langle a, \varphi \rangle.$$
>
> The DeepMind prover agent provided a formal proof, showing that $\frac{183095}{30000}$ separates the
> support functions.

```lean
theorem green_57.variants.z3_functional :
    let a : ZMod 3 → ℂ := ![(-1 : ℂ), -3, 3]
    supportFn (ZMod 3) a (Φ' (ZMod 3)) < supportFn (ZMod 3) a (Φ (ZMod 3))
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/GreensOpenProblems/57.lean, line 112](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/57.lean#L112).

## `Green57.green_57.variants.z3`

Solved: stated here; a Lean proof is at [https://github.com/mo271/formal-conjectures/blob/f5afe85e1e02611f63c32ae041b33c67b7938cba/FormalConjectures/GreensOpenProblems/57.lean#L1100](https://github.com/mo271/formal-conjectures/blob/f5afe85e1e02611f63c32ae041b33c67b7938cba/FormalConjectures/GreensOpenProblems/57.lean#L1100).

> Do $\Phi(\mathbb{Z}/3\mathbb{Z})$ and $\Phi'(\mathbb{Z}/3\mathbb{Z})$ coincide?
>
> Numerical evidence suggests the answer is **no**: the integer functional $a = (-1, -3, 3)$
> separates the two spaces. A branch-and-bound verification over the phase variables shows
> $\max_{\Phi'} \operatorname{Re}\langle a, \varphi \rangle < 6.112 < 6.115 \approx
> \max_{\Phi} \operatorname{Re}\langle a, \varphi \rangle$.

```lean
theorem green_57.variants.z3 :
    ¬ (Φ (ZMod 3) = Φ' (ZMod 3))
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/GreensOpenProblems/57.lean, line 127](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/57.lean#L127).

## `Green57.green_57`

Solved: stated here; a Lean proof is at [https://github.com/mo271/formal-conjectures/blob/f5afe85e1e02611f63c32ae041b33c67b7938cba/FormalConjectures/GreensOpenProblems/57.lean#L1120](https://github.com/mo271/formal-conjectures/blob/f5afe85e1e02611f63c32ae041b33c67b7938cba/FormalConjectures/GreensOpenProblems/57.lean#L1120).

> Is it true that for every finite abelian group $G$ the spaces $\Phi(G)$ and $\Phi'(G)$,
> obtained from kernels $\phi(g) = \mathbb{E}_{x_1 + x_2 + x_3 = g} f_1(x_2, x_3)
>       f_2(x_1, x_3) f_3(x_1, x_2)$ with $\lVert f_i \rVert_\infty \le 1$
> (where $f_i : G \times G \to \mathbb{C}$), still coincide when the
> third kernel is required to depend only on $x_1 + x_2$?
>
> Green guesses that the answer is probably 'no'.

```lean
theorem green_57 :
    ¬ ∀ (G : Type) [AddCommGroup G] [Fintype G] [DecidableEq G],
      Φ G = Φ' G
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/GreensOpenProblems/57.lean, line 142](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/57.lean#L142).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/GreensOpenProblems/57.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/57.lean)
- [Ben Green's Open Problem 57](https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf#section.8)
