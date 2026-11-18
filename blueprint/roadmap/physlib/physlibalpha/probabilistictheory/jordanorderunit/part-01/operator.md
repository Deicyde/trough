---
declaration: module
origin: cited
lean: ProbabilisticTheory.JordanAlgebra.jpow, ProbabilisticTheory.JordanAlgebra.jpow_zero, ProbabilisticTheory.JordanAlgebra.jpow_succ, ProbabilisticTheory.JordanAlgebra.jpow_one, ProbabilisticTheory.JordanAlgebra.jpow_two, ProbabilisticTheory.JordanAlgebra.mulLeft, ProbabilisticTheory.JordanAlgebra.mulLeft_apply, ProbabilisticTheory.JordanAlgebra.mulLeft_one
statement: formalized
proof: formalized
---

# Powers, multiplication operators and the quadratic representation

The module `PhyslibAlpha.ProbabilisticTheory.JordanOrderUnit.Operator`, [PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Operator.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Operator.lean): 56 declarations, 42 with a docstring.

> Jordan powers, multiplication operators `L_a` and the quadratic representation `U_a`.

## i. Overview

> Powers of an observable are `a⁰ = 1` and `aⁿ⁺¹ = a ∘ aⁿ`. The multiplication operator is `L\_a b = a
> ∘ b`, and the quadratic representation `U\_a = 2 L\_a² - L\_\{a²}` is the Jordan version of `b ↦ a b a`.
> The Jordan identity says that `L_a` and `L_{a²}` commute.

## ii. Key results

> - `JordanAlgebra.jpow` : powers.
> - `JordanAlgebra.mulLeft` : the multiplication operator `L_a`.
> - `JordanAlgebra.quadRep` : the quadratic representation `U_a`.

## iv. References

> * None.

## A. Powers

**`ProbabilisticTheory.JordanAlgebra.jpow`**, a def, [line 54](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Operator.lean#L54).

> The `n`-th Jordan power of `a`, defined by the fixed left-bracketing recursion
> `a^[0] = 1`, `a^[n+1] = a ∘ a^[n]`.

```lean
def jpow (a : E) : ℕ → E
```

**`ProbabilisticTheory.JordanAlgebra.jpow_zero`**, a lemma, [line 60](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Operator.lean#L60).

```lean
lemma jpow_zero (a : E) : a ^[0] = 1
```

**`ProbabilisticTheory.JordanAlgebra.jpow_succ`**, a lemma, [line 62](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Operator.lean#L62).

```lean
lemma jpow_succ (a : E) (n : ℕ) : a ^[n + 1] = a * a ^[n]
```

**`ProbabilisticTheory.JordanAlgebra.jpow_one`**, a lemma, [line 64](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Operator.lean#L64).

```lean
lemma jpow_one (a : E) : a ^[1] = a
```

**`ProbabilisticTheory.JordanAlgebra.jpow_two`**, a lemma, [line 68](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Operator.lean#L68).

> The second Jordan power is the Jordan square, `a ∘ a`.

```lean
lemma jpow_two (a : E) : a ^[2] = a * a
```

## B. The multiplication operator `L_a`

**`ProbabilisticTheory.JordanAlgebra.mulLeft`**, a def, [line 80](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Operator.lean#L80).

> The Jordan multiplication operator `L a : E →ₗ[ℝ] E`, `L a b = a ∘ b`. Linear in `b` since the
> Jordan product distributes over `+` (`NonUnitalNonAssocCommRing`) and commutes with real scalars
> (`SMulCommClass ℝ E E`).

```lean
def mulLeft (a : E) : E →ₗ[ℝ] E
```

**`ProbabilisticTheory.JordanAlgebra.mulLeft_apply`**, a lemma, [line 87](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Operator.lean#L87).

```lean
lemma mulLeft_apply (a b : E) : L a b = a * b
```

**`ProbabilisticTheory.JordanAlgebra.mulLeft_one`**, a lemma, [line 89](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Operator.lean#L89).

```lean
lemma mulLeft_one (a : E) : L a 1 = a
```

**`ProbabilisticTheory.JordanAlgebra.mulLeft_one_apply`**, a lemma, [line 91](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Operator.lean#L91).

```lean
lemma mulLeft_one_apply (a : E) : L 1 a = a
```

## C. The quadratic representation `U_a`

**`ProbabilisticTheory.JordanAlgebra.quadRep`**, a def, [line 96](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Operator.lean#L96).

> The quadratic representation `U_a = 2 L_a² - L_{a²}`, the Jordan version of `b ↦ a b a`.

```lean
def quadRep (a : E) : E →ₗ[ℝ] E
```

**`ProbabilisticTheory.JordanAlgebra.quadRep_apply`**, a lemma, [line 101](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Operator.lean#L101).

```lean
lemma quadRep_apply (a b : E) : U a b = (2 : ℝ) • (a * (a * b)) - a ^[2] * b
```

**`ProbabilisticTheory.JordanAlgebra.quadRep_zero_apply`**, a lemma, [line 104](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Operator.lean#L104).

```lean
lemma quadRep_zero_apply (b : E) : U (0 : E) b = 0
```

**`ProbabilisticTheory.JordanAlgebra.quadRep_add_right`**, a lemma, [line 108](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Operator.lean#L108).

```lean
lemma quadRep_add_right (a b c : E) : U a (b + c) = U a b + U a c
```

**`ProbabilisticTheory.JordanAlgebra.quadRep_smul_right`**, a lemma, [line 111](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Operator.lean#L111).

```lean
lemma quadRep_smul_right (r : ℝ) (a b : E) : U a (r • b) = r • U a b
```

**`ProbabilisticTheory.JordanAlgebra.quadRepPolar`**, a def, [line 116](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Operator.lean#L116).

> The polarization of the quadratic representation, `x ↦ a x b + b x a` in the associative case.

```lean
def quadRepPolar (a b : E) : E →ₗ[ℝ] E
```

**`ProbabilisticTheory.JordanAlgebra.quadRepBilin`**, a def, [line 122](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Operator.lean#L122).

> The standard bilinear quadratic operator.  `quadRepPolar` is its literal cross-effect
> and therefore equals twice this operator.  Keeping this undivided normalization is essential for
> the finite polarization identities used in the algebraic proof of the fundamental formula.

```lean
def quadRepBilin (a b : E) : E →ₗ[ℝ] E
```

**`ProbabilisticTheory.JordanAlgebra.quadRepBilin_apply`**, a lemma, [line 126](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Operator.lean#L126).

> Pointwise form of the standard bilinear quadratic operator.

```lean
lemma quadRepBilin_apply (a b x : E) :
    quadRepBilin a b x = a * (b * x) + b * (a * x) - (a * b) * x
```

**`ProbabilisticTheory.JordanAlgebra.quadRepBilin_comm`**, a lemma, [line 132](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Operator.lean#L132).

> The standard bilinear quadratic operator is symmetric.

```lean
lemma quadRepBilin_comm (a b : E) : quadRepBilin a b = quadRepBilin b a
```

**`ProbabilisticTheory.JordanAlgebra.quadRepBilin_add_left`**, a lemma, [line 138](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Operator.lean#L138).

> Additivity in the first variable of the standard quadratic polarization.

```lean
lemma quadRepBilin_add_left (a b c : E) :
    quadRepBilin (a + b) c = quadRepBilin a c + quadRepBilin b c
```

**`ProbabilisticTheory.JordanAlgebra.quadRepBilin_smul_left`**, a lemma, [line 149](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Operator.lean#L149).

> Real linearity in the first variable of the standard quadratic polarization.

```lean
lemma quadRepBilin_smul_left (r : ℝ) (a b : E) :
    quadRepBilin (r • a) b = r • quadRepBilin a b
```

**`ProbabilisticTheory.JordanAlgebra.quadRepBilin_add_right`**, a lemma, [line 166](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Operator.lean#L166).

> Additivity in the second variable of the standard quadratic polarization.

```lean
lemma quadRepBilin_add_right (a b c : E) :
    quadRepBilin a (b + c) = quadRepBilin a b + quadRepBilin a c
```

**`ProbabilisticTheory.JordanAlgebra.quadRepBilin_smul_right`**, a lemma, [line 172](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Operator.lean#L172).

> Real linearity in the second variable of the standard quadratic polarization.

```lean
lemma quadRepBilin_smul_right (r : ℝ) (a b : E) :
    quadRepBilin a (r • b) = r • quadRepBilin a b
```

**`ProbabilisticTheory.JordanAlgebra.quadRepBilin_neg_right`**, a lemma, [line 180](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Operator.lean#L180).

> Signed second-variable specialization of the bilinear quadratic operator.

```lean
lemma quadRepBilin_neg_right (a b : E) :
    quadRepBilin a (-b) = -quadRepBilin a b
```

**`ProbabilisticTheory.JordanAlgebra.quadRepBilin_neg_left`**, a lemma, [line 185](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Operator.lean#L185).

> Signed first-variable specialization of the bilinear quadratic operator.

```lean
lemma quadRepBilin_neg_left (a b : E) :
    quadRepBilin (-a) b = -quadRepBilin a b
```

**`ProbabilisticTheory.JordanAlgebra.quadRepBilin_sub_right`**, a lemma, [line 193](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Operator.lean#L193).

> Difference expansion in the second variable of the bilinear quadratic operator.

```lean
lemma quadRepBilin_sub_right (a b c : E) :
    quadRepBilin a (b - c) = quadRepBilin a b - quadRepBilin a c
```

**`ProbabilisticTheory.JordanAlgebra.quadRepPolar_eq_two_smul_quadRepBilin`**, a lemma, [line 199](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Operator.lean#L199).

> The cross-effect normalization is twice the standard bilinear quadratic operator.

```lean
lemma quadRepPolar_eq_two_smul_quadRepBilin (a b : E) :
    quadRepPolar a b = (2 : ℝ) • quadRepBilin a b
```

**`ProbabilisticTheory.JordanAlgebra.quadRepBilin_self`**, a lemma, [line 204](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Operator.lean#L204).

> The diagonal of the standard bilinear quadratic operator is the quadratic representation.

```lean
lemma quadRepBilin_self (a : E) : quadRepBilin a a = U a
```

**`ProbabilisticTheory.JordanAlgebra.quadRepPolar_apply`**, a lemma, [line 213](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Operator.lean#L213).

> Pointwise form of the polarized quadratic representation.

```lean
lemma quadRepPolar_apply (a b x : E) :
    quadRepPolar a b x =
      (2 : ℝ) • (a * (b * x) + b * (a * x) - (a * b) * x)
```

**`ProbabilisticTheory.JordanAlgebra.quadRepPolar_comm`**, a lemma, [line 220](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Operator.lean#L220).

> Polarization is symmetric in its two outer variables.

```lean
lemma quadRepPolar_comm (a b : E) : quadRepPolar a b = quadRepPolar b a
```

**`ProbabilisticTheory.JordanAlgebra.quadRepPolar_add_left`**, a lemma, [line 226](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Operator.lean#L226).

> The polarization is additive in its first outer variable.

```lean
lemma quadRepPolar_add_left (a b c : E) :
    quadRepPolar (a + b) c = quadRepPolar a c + quadRepPolar b c
```

**`ProbabilisticTheory.JordanAlgebra.quadRepPolar_smul_left`**, a lemma, [line 237](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Operator.lean#L237).

> The polarization is real-linear in its first outer variable.

```lean
lemma quadRepPolar_smul_left (r : ℝ) (a b : E) :
    quadRepPolar (r • a) b = r • quadRepPolar a b
```

**`ProbabilisticTheory.JordanAlgebra.quadRepPolar_add_right`**, a lemma, [line 255](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Operator.lean#L255).

> The polarization is additive in its second outer variable.

```lean
lemma quadRepPolar_add_right (a b c : E) :
    quadRepPolar a (b + c) = quadRepPolar a b + quadRepPolar a c
```

**`ProbabilisticTheory.JordanAlgebra.quadRepPolar_smul_right`**, a lemma, [line 261](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Operator.lean#L261).

> The polarization is real-linear in its second outer variable.

```lean
lemma quadRepPolar_smul_right (r : ℝ) (a b : E) :
    quadRepPolar a (r • b) = r • quadRepPolar a b
```

**`ProbabilisticTheory.JordanAlgebra.quadRepPolar_self`**, a lemma, [line 269](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Operator.lean#L269).

> The diagonal of the polarization is twice the original quadratic representation.

```lean
lemma quadRepPolar_self (a : E) : quadRepPolar a a = (2 : ℝ) • U a
```

**`ProbabilisticTheory.JordanAlgebra.quadRep_add_apply`**, a lemma, [line 280](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Operator.lean#L280).

> The quadratic representation splits into its two diagonal pieces and its polarized
> cross-effect.

```lean
lemma quadRep_add_apply (a b x : E) :
    U (a + b) x = U a x + quadRepPolar a b x + U b x
```

**`ProbabilisticTheory.JordanAlgebra.quadRep_add_eq`**, a lemma, [line 289](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Operator.lean#L289).

> Exact additive polarization of the quadratic representation in standard normalization.

```lean
lemma quadRep_add_eq (a b : E) :
    U (a + b) = U a + (2 : ℝ) • quadRepBilin a b + U b
```

**`ProbabilisticTheory.JordanAlgebra.quadRep_sub_eq`**, a lemma, [line 297](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Operator.lean#L297).

> Signed additive polarization, obtained from the same quadratic cross-effect.  Together with
> `quadRep_add_eq`, this gives the two exact evaluations used to isolate a quadratic coefficient.

```lean
lemma quadRep_sub_eq (a b : E) :
    U (a - b) = U a - (2 : ℝ) • quadRepBilin a b + U b
```

**`ProbabilisticTheory.JordanAlgebra.quadRep_add_add_eq`**, a lemma, [line 310](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Operator.lean#L310).

> The quadratic representation of a three-term sum, expressed through the canonical symmetric
> bilinear cross-effect.  This is the coefficient-expansion interface for polarizing identities in
> quadratic representations; it keeps all mixed terms in the single `quadRepBilin` API.

```lean
lemma quadRep_add_add_eq (a b c : E) :
    U (a + b + c) =
      U a + U b + U c +
        (2 : ℝ) • quadRepBilin a b +
          (2 : ℝ) • quadRepBilin a c +
            (2 : ℝ) • quadRepBilin b c
```

**`ProbabilisticTheory.JordanAlgebra.add_mul_self`**, a lemma, [line 321](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Operator.lean#L321).

> Exact square expansion for the positive polarization evaluation.

```lean
lemma add_mul_self (a b : E) :
    (a + b) * (a + b) = a * a + (2 : ℝ) • (a * b) + b * b
```

**`ProbabilisticTheory.JordanAlgebra.sub_mul_self`**, a lemma, [line 329](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Operator.lean#L329).

> Exact square expansion for the signed polarization evaluation.

```lean
lemma sub_mul_self (a b : E) :
    (a - b) * (a - b) = a * a - (2 : ℝ) • (a * b) + b * b
```

**`ProbabilisticTheory.JordanAlgebra.quadRep_smul_apply`**, a lemma, [line 336](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Operator.lean#L336).

> Quadratic representations are homogeneous of degree two in their outer argument.

```lean
lemma quadRep_smul_apply (r : ℝ) (a b : E) :
    U (r • a) b = r ^ 2 • U a b
```

**`ProbabilisticTheory.JordanAlgebra.quadRep_smul_eq`**, a lemma, [line 342](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Operator.lean#L342).

> Quadratic homogeneity of the representation, as an equality of operators.

```lean
lemma quadRep_smul_eq (r : ℝ) (a : E) :
    U (r • a) = r ^ 2 • U a
```

**`ProbabilisticTheory.JordanAlgebra.quadRep_neg_apply`**, a lemma, [line 348](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Operator.lean#L348).

```lean
lemma quadRep_neg_apply (a b : E) : U (-a) b = U a b
```

**`ProbabilisticTheory.JordanAlgebra.quadRep_neg`**, a lemma, [line 352](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Operator.lean#L352).

> Sign invariance of the quadratic representation, as an equality of operators.

```lean
lemma quadRep_neg (a : E) : U (-a) = U a
```

**`ProbabilisticTheory.JordanAlgebra.quadRep_one_apply`**, a lemma, [line 358](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Operator.lean#L358).

> The quadratic representation of the order unit is the identity: `U_1 = id`. The Jordan
> identity element acts as "conjugate by the identity", i.e. does nothing.

```lean
lemma quadRep_one_apply (b : E) : U (1 : E) b = b
```

**`ProbabilisticTheory.JordanAlgebra.quadRep_one_comp`**, a lemma, [line 366](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Operator.lean#L366).

```lean
lemma quadRep_one_comp (a : E) : (U (1 : E)).comp (U a) = U a
```

**`ProbabilisticTheory.JordanAlgebra.quadRep_comp_one`**, a lemma, [line 370](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Operator.lean#L370).

```lean
lemma quadRep_comp_one (a : E) : (U a).comp (U (1 : E)) = U a
```

**`ProbabilisticTheory.JordanAlgebra.quadRep_apply_one`**, a lemma, [line 377](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Operator.lean#L377).

> The quadratic representation of `a`, evaluated at the order unit, recovers the Jordan square:
> `U_a(1) = a²`. Conjugating the identity by `a` gives back `a²`, matching the associative picture
> `a \cdot 1 \cdot a = a^2`.

```lean
lemma quadRep_apply_one (a : E) : U a (1 : E) = a ^[2]
```

## D. The Jordan commutation law

**`ProbabilisticTheory.JordanAlgebra.quadRep_mulLeft`**, a lemma, [line 386](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Operator.lean#L386).

> `U_a` commutes with `L_a`.

```lean
lemma quadRep_mulLeft [IsCommJordan E] (a x : E) : U a (a * x) = a * U a x
```

**`ProbabilisticTheory.JordanAlgebra.quadRep_mulLeft_sq`**, a lemma, [line 397](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Operator.lean#L397).

> Quadratic representation by `a` also commutes with multiplication by the square `a²`.
> Together with `quadRep_mulLeft`, this says that `U_a` preserves the associative algebra generated
> by `a` at the operator level, without appealing to an ambient associative realization.

```lean
lemma quadRep_mulLeft_sq [IsCommJordan E] (a x : E) :
    U a (a ^[2] * x) = a ^[2] * U a x
```

**`ProbabilisticTheory.JordanAlgebra.commute_quadRep_mulLeft`**, a lemma, [line 406](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Operator.lean#L406).

> Bundled form of `quadRep_mulLeft`: the quadratic representation commutes with `L_a`.

```lean
lemma commute_quadRep_mulLeft [IsCommJordan E] (a : E) : Commute (U a) (L a)
```

**`ProbabilisticTheory.JordanAlgebra.commute_quadRep_mulLeft_sq`**, a lemma, [line 411](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Operator.lean#L411).

> Bundled form of `quadRep_mulLeft_sq`: the quadratic representation commutes with `L_(a²)`.

```lean
lemma commute_quadRep_mulLeft_sq [IsCommJordan E] (a : E) : Commute (U a) (L (a ^[2]))
```

## E. The inner derivation `D_{a,b}`

**`ProbabilisticTheory.JordanAlgebra.innerDerivation`**, a def, [line 418](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Operator.lean#L418).

> The inner derivation `D_{a,b} = [L_a, L_b]`.

```lean
def innerDerivation (a b : E) : E →ₗ[ℝ] E
```

**`ProbabilisticTheory.JordanAlgebra.innerDerivation_apply`**, a lemma, [line 421](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Operator.lean#L421).

> Pointwise form of the inner derivation.

```lean
lemma innerDerivation_apply (a b x : E) : innerDerivation a b x = a * (b * x) - b * (a * x)
```

**`ProbabilisticTheory.JordanAlgebra.innerDerivation_swap`**, a lemma, [line 425](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Operator.lean#L425).

> The inner derivation is antisymmetric in its two defining arguments.

```lean
lemma innerDerivation_swap (a b : E) : innerDerivation a b = -innerDerivation b a
```

**`ProbabilisticTheory.JordanAlgebra.innerDerivation_self`**, a lemma, [line 430](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Operator.lean#L430).

```lean
lemma innerDerivation_self (a : E) : innerDerivation a a = 0
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Operator.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Operator.lean)
