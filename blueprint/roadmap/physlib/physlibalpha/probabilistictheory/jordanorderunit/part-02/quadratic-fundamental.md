---
declaration: module
origin: cited
lean: ProbabilisticTheory.JordanAlgebra.cyclic_mulLeft_commutator, ProbabilisticTheory.JordanAlgebra.cyclic_mulLeft_assoc_sum, ProbabilisticTheory.JordanAlgebra.mulLeft_triple_normalize, ProbabilisticTheory.JordanAlgebra.mulLeft_cube_normalize, ProbabilisticTheory.JordanAlgebra.mul_self_mul_self_mulLeft_normalize, ProbabilisticTheory.JordanAlgebra.quadRep_mul_self_eq_comp, ProbabilisticTheory.JordanAlgebra.quadRep_add_mul_self_eq_comp, ProbabilisticTheory.JordanAlgebra.quadRep_add_square_polarized
statement: formalized
proof: formalized
---

# The fundamental formula

The module `PhyslibAlpha.ProbabilisticTheory.JordanOrderUnit.Quadratic.Fundamental`, [PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Quadratic/Fundamental.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Quadratic/Fundamental.lean): 35 declarations, 35 with a docstring.

> The fundamental formula `U_{U_a b} = U_a U_b U_a`, proved from the Jordan identity alone.

## i. Overview

> The quadratic representation satisfies the fundamental formula `U_{U_a b} = U_a U_b U_a`. The proof
> uses only the Jordan identity, through the inner derivations `[L_a, L_b]` and the triple operators.

## ii. Key results

> - `JordanAlgebra.quadRep_quadRep_eq` : `U_{a²} = U_a²`.
> - `JordanAlgebra.quadRep_fundamental` : **the fundamental formula** `U_{U_a b} = U_a U_b U_a`.

## iv. References

> * None.

## A. Fundamental composition identity

**`ProbabilisticTheory.JordanAlgebra.cyclic_mulLeft_commutator`**, a lemma, [line 56](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Quadratic/Fundamental.lean#L56).

> The polarized Jordan identity, evaluated at a fourth element.

```lean
lemma cyclic_mulLeft_commutator (a b c x : E) :
    (a * ((b * c) * x) - (b * c) * (a * x)) +
        (b * ((c * a) * x) - (c * a) * (b * x)) +
          (c * ((a * b) * x) - (a * b) * (c * x)) = 0
```

**`ProbabilisticTheory.JordanAlgebra.cyclic_mulLeft_assoc_sum`**, a lemma, [line 81](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Quadratic/Fundamental.lean#L81).

> The polarized Jordan identity with its three commutators collected.

```lean
lemma cyclic_mulLeft_assoc_sum (a b c x : E) :
    a * ((b * c) * x) + b * ((c * a) * x) + c * ((a * b) * x) =
      (b * c) * (a * x) + (c * a) * (b * x) + (a * b) * (c * x)
```

**`ProbabilisticTheory.JordanAlgebra.mulLeft_triple_normalize`**, a lemma, [line 94](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Quadratic/Fundamental.lean#L94).

> The multiplication operator of a triple product in terms of multiplication operators of single
> and double products.

```lean
lemma mulLeft_triple_normalize (a b c : E) :
    L (a * (b * c)) =
      ((L a).comp (L (b * c)) + (L b).comp (L (a * c)) + (L c).comp (L (a * b))) -
        (((L b).comp (L a)).comp (L c) + ((L c).comp (L a)).comp (L b))
```

**`ProbabilisticTheory.JordanAlgebra.mulLeft_cube_normalize`**, a lemma, [line 125](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Quadratic/Fundamental.lean#L125).

> First specialization of `mulLeft_triple_normalize`: the multiplication operator of the third
> Jordan power is a polynomial in `L_a` and `L_(a²)`.

```lean
lemma mulLeft_cube_normalize (a : E) :
    L (a * (a * a)) =
      (3 : ℝ) • ((L a).comp (L (a * a))) -
        (2 : ℝ) • (((L a).comp (L a)).comp (L a))
```

**`ProbabilisticTheory.JordanAlgebra.mul_self_mul_self_mulLeft_normalize`**, a lemma, [line 134](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Quadratic/Fundamental.lean#L134).

> Second normalization step, evaluated at `x`: multiplication by `(a²)²` is reduced to the
> commuting operators `L_a` and `L_(a²)`.

```lean
lemma mul_self_mul_self_mulLeft_normalize (a x : E) :
    ((a * a) * (a * a)) * x =
      (a * a) * ((a * a) * x) +
        (4 : ℝ) • (a * (a * ((a * a) * x))) -
          (4 : ℝ) • (a * (a * (a * (a * x))))
```

**`ProbabilisticTheory.JordanAlgebra.quadRep_mul_self_eq_comp`**, a lemma, [line 167](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Quadratic/Fundamental.lean#L167).

> The quadratic representation of a Jordan square is the square of its quadratic
> representation. This is the first nontrivial quadratic fundamental identity; its proof uses only
> the finite operator normalization certificate and the Jordan commutation law.

```lean
lemma quadRep_mul_self_eq_comp (a : E) :
    U (a * a) = (U a).comp (U a)
```

**`ProbabilisticTheory.JordanAlgebra.quadRep_add_mul_self_eq_comp`**, a lemma, [line 186](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Quadratic/Fundamental.lean#L186).

> The square identity evaluated on a sum.  This keeps the polarizing source equation in a
> canonical bilinear form: the remaining coefficient extraction is purely a finite calculation in
> the noncommutative ring of linear endomorphisms.

```lean
lemma quadRep_add_mul_self_eq_comp (a b : E) :
    U ((a + b) * (a + b)) =
      (U a + (2 : ℝ) • quadRepBilin a b + U b).comp
        (U a + (2 : ℝ) • quadRepBilin a b + U b)
```

**`ProbabilisticTheory.JordanAlgebra.quadRep_add_square_polarized`**, a lemma, [line 196](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Quadratic/Fundamental.lean#L196).

> The positive polarization of the square identity, fully expanded in the canonical bilinear
> quadratic operator.  Pairing this equation with its signed counterpart isolates the standard
> mixed quadratic coefficient.

```lean
lemma quadRep_add_square_polarized (a b : E) :
    (U a).comp (U a) + (4 : ℝ) • U (a * b) + (U b).comp (U b) +
          (4 : ℝ) • quadRepBilin (a * a) (a * b) +
            (2 : ℝ) • quadRepBilin (a * a) (b * b) +
              (4 : ℝ) • quadRepBilin (a * b) (b * b) =
      (U a).comp (U a) + (4 : ℝ) • (quadRepBilin a b).comp (quadRepBilin a b) +
          (U b).comp (U b) + (U a).comp (U b) + (U b).comp (U a) +
            (2 : ℝ) • ((U a).comp (quadRepBilin a b) +
              (quadRepBilin a b).comp (U a) + (U b).comp (quadRepBilin a b) +
                (quadRepBilin a b).comp (U b))
```

**`ProbabilisticTheory.JordanAlgebra.quadRep_sub_square_polarized`**, a lemma, [line 217](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Quadratic/Fundamental.lean#L217).

> The signed companion to `quadRep_add_square_polarized`.  Adding the two equations cancels
> the cubic terms and leaves precisely the mixed quadratic coefficient.

```lean
lemma quadRep_sub_square_polarized (a b : E) :
    (U a).comp (U a) + (4 : ℝ) • U (a * b) + (U b).comp (U b) -
          (4 : ℝ) • quadRepBilin (a * a) (a * b) +
            (2 : ℝ) • quadRepBilin (a * a) (b * b) -
              (4 : ℝ) • quadRepBilin (a * b) (b * b) =
      (U a).comp (U a) + (4 : ℝ) • (quadRepBilin a b).comp (quadRepBilin a b) +
          (U b).comp (U b) + (U a).comp (U b) + (U b).comp (U a) -
            (2 : ℝ) • ((U a).comp (quadRepBilin a b) +
              (quadRepBilin a b).comp (U a) + (U b).comp (quadRepBilin a b) +
                (quadRepBilin a b).comp (U b))
```

**`ProbabilisticTheory.JordanAlgebra.quadRepBilin_comp_self_polarization`**, a lemma, [line 233](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Quadratic/Fundamental.lean#L233).

> The mixed polarization of the quadratic representation.

```lean
lemma quadRepBilin_comp_self_polarization (a b : E) :
    (4 : ℝ) • (quadRepBilin a b).comp (quadRepBilin a b) =
      (4 : ℝ) • U (a * b) + (2 : ℝ) • quadRepBilin (a * a) (b * b) -
        (U a).comp (U b) - (U b).comp (U a)
```

## B. Polarizing the cubic commutation law: the triple commutator identity

**`ProbabilisticTheory.JordanAlgebra.quadRep_add_apply'`**, a lemma, [line 267](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Quadratic/Fundamental.lean#L267).

> Pointwise expansion of `U (a + b)` at an arbitrary argument, the elementary consequence of
> `quadRep_add_eq` used repeatedly below to unfold both sides of the polarized cubic law.

```lean
lemma quadRep_add_apply' (a b y : E) :
    U (a + b) y = U a y + (2 : ℝ) • quadRepBilin a b y + U b y
```

**`ProbabilisticTheory.JordanAlgebra.quadRep_sub_apply'`**, a lemma, [line 274](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Quadratic/Fundamental.lean#L274).

> Pointwise expansion of `U (a - b)` at an arbitrary argument.

```lean
lemma quadRep_sub_apply' (a b y : E) :
    U (a - b) y = U a y - (2 : ℝ) • quadRepBilin a b y + U b y
```

**`ProbabilisticTheory.JordanAlgebra.quadRepBilin_mulLeft_polarization`**, a lemma, [line 280](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Quadratic/Fundamental.lean#L280).

> The `(2, 1)`-component of `U_{a + b}` commuting with `L_{a + b}`.

```lean
lemma quadRepBilin_mulLeft_polarization (a b x : E) :
    U a (b * x) + (2 : ℝ) • quadRepBilin a b (a * x) =
      b * U a x + (2 : ℝ) • (a * quadRepBilin a b x)
```

**`ProbabilisticTheory.JordanAlgebra.quadRepBilin_mulLeft_polarization'`**, a lemma, [line 293](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Quadratic/Fundamental.lean#L293).

> The `(1, 2)`-component of `U_{a + b}` commuting with `L_{a + b}`.

```lean
lemma quadRepBilin_mulLeft_polarization' (a b x : E) :
    U b (a * x) + (2 : ℝ) • quadRepBilin a b (b * x) =
      a * U b x + (2 : ℝ) • (b * quadRepBilin a b x)
```

## C. Normalizing the multiplication operator of a quadratic image

**`ProbabilisticTheory.JordanAlgebra.mulLeft_quadRep_normalize`**, a lemma, [line 302](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Quadratic/Fundamental.lean#L302).

> `L_{U_a b}` in terms of `L_a`, `L_b`, `L_{a²}` and `L_{a ∘ b}`.

```lean
lemma mulLeft_quadRep_normalize (a b : E) :
    L (U a b) =
      (2 : ℝ) • ((L a).comp (L (a * b))) + (L b).comp (L (a * a)) -
        (2 : ℝ) • (((L a).comp (L a)).comp (L b)) -
          (2 : ℝ) • (((L b).comp (L a)).comp (L a)) +
            (2 : ℝ) • (((L a).comp (L b)).comp (L a))
```

**`ProbabilisticTheory.JordanAlgebra.quadRep_quadRep_eq`**, a lemma, [line 328](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Quadratic/Fundamental.lean#L328).

> `U_{U_a b}` in terms of the quadratic representations of `a ∘ (a ∘ b)` and `a² ∘ b`.

```lean
lemma quadRep_quadRep_eq (a b : E) :
    U (U a b) =
      (4 : ℝ) • U (a * (a * b)) - (4 : ℝ) • quadRepBilin (a * (a * b)) (jpow a 2 * b) +
        U (jpow a 2 * b)
```

## D. The inner derivation and the Jordan-triple-system fundamental identity

> With the inner derivations `D_{a,b} = [L_a, L_b]` and the triple operators `V\_\{a,b} = L\_\{a ∘ b} +
> D\_\{a,b}`, the fundamental identity of Jordan triple systems follows from the fact that inner
> derivations are derivations of the Jordan product.

**`ProbabilisticTheory.JordanAlgebra.innerDerivation_add_left`**, a lemma, [line 354](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Quadratic/Fundamental.lean#L354).

> Additivity of the inner derivation in its first defining argument.

```lean
lemma innerDerivation_add_left (a b c : E) :
    innerDerivation (a + b) c = innerDerivation a c + innerDerivation b c
```

**`ProbabilisticTheory.JordanAlgebra.innerDerivation_smul_left`**, a lemma, [line 363](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Quadratic/Fundamental.lean#L363).

> Real linearity of the inner derivation in its first defining argument.

```lean
lemma innerDerivation_smul_left (r : ℝ) (a b : E) :
    innerDerivation (r • a) b = r • innerDerivation a b
```

**`ProbabilisticTheory.JordanAlgebra.innerDerivation_add_right`**, a lemma, [line 377](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Quadratic/Fundamental.lean#L377).

> Additivity of the inner derivation in its second defining argument.

```lean
lemma innerDerivation_add_right (a b c : E) :
    innerDerivation a (b + c) = innerDerivation a b + innerDerivation a c
```

**`ProbabilisticTheory.JordanAlgebra.innerDerivation_smul_right`**, a lemma, [line 387](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Quadratic/Fundamental.lean#L387).

> Real linearity of the inner derivation in its second defining argument.

```lean
lemma innerDerivation_smul_right (r : ℝ) (a b : E) :
    innerDerivation a (r • b) = r • innerDerivation a b
```

**`ProbabilisticTheory.JordanAlgebra.innerDerivation_sub_left`**, a lemma, [line 393](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Quadratic/Fundamental.lean#L393).

> Difference expansion of the inner derivation in its first defining argument.

```lean
lemma innerDerivation_sub_left (a b c : E) :
    innerDerivation (a - b) c = innerDerivation a c - innerDerivation b c
```

**`ProbabilisticTheory.JordanAlgebra.jordanTriple_diag_left`**, a lemma, [line 404](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Quadratic/Fundamental.lean#L404).

> The diagonal fact for the triple product at `(a, a, x)`: telescoping cancellation collapses
> it to the plain associative square multiplication `a² x`.  This is the base case used in the
> final specialization of the fundamental identity.

```lean
lemma jordanTriple_diag_left (a x : E) : jordanTriple a a x = a ^[2] * x
```

**`ProbabilisticTheory.JordanAlgebra.innerDerivation_mul`**, a lemma, [line 410](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Quadratic/Fundamental.lean#L410).

> **Inner derivations are derivations**: `D_{a,b} (x ∘ y) = D_{a,b} x ∘ y + x ∘ D_{a,b} y`.

```lean
lemma innerDerivation_mul (a b x y : E) :
    innerDerivation a b (x * y) = (innerDerivation a b x) * y + x * (innerDerivation a b y)
```

**`ProbabilisticTheory.JordanAlgebra.innerDerivation_mulLeft_comm`**, a lemma, [line 421](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Quadratic/Fundamental.lean#L421).

> The derivation property restated as an operator commutator: `[D_{a,b}, L_x] = L_{D_{a,b} x}`.
> This is `innerDerivation_mul` read as a statement about composed multiplication operators; it is
> the operator-level form used to build the double commutator `innerDerivation_comm` below.

```lean
lemma innerDerivation_mulLeft_comm (a b x : E) :
    (innerDerivation a b).comp (L x) - (L x).comp (innerDerivation a b) =
      L (innerDerivation a b x)
```

**`ProbabilisticTheory.JordanAlgebra.innerDerivation_comm`**, a lemma, [line 430](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Quadratic/Fundamental.lean#L430).

> `[D_{a,b}, D_{c,d}] = D_{D_{a,b} c, d} + D_{c, D_{a,b} d}`.

```lean
lemma innerDerivation_comm (a b c d : E) :
    (innerDerivation a b).comp (innerDerivation c d) -
        (innerDerivation c d).comp (innerDerivation a b) =
      innerDerivation (innerDerivation a b c) d + innerDerivation c (innerDerivation a b d)
```

**`ProbabilisticTheory.JordanAlgebra.tripleOperator`**, a def, [line 448](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Quadratic/Fundamental.lean#L448).

> The Jordan triple operator `V_{a,b} := L_{a*b} + D_{a,b}`.  Its action on any `x` is exactly
> the Jordan triple product `{a,b,x}` (`triple_eq_V_apply`), so it packages `jordanTriple`'s middle
> slot as a bundled linear operator, mirroring how `quadRepBilin a c` already packages `{a,·,c}`.

```lean
def tripleOperator (a b : E) : E →ₗ[ℝ] E
```

**`ProbabilisticTheory.JordanAlgebra.triple_eq_V_apply`**, a lemma, [line 454](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Quadratic/Fundamental.lean#L454).

> The Jordan triple operator `V_{a,b}` computes the Jordan triple product in its middle slot.

```lean
lemma triple_eq_V_apply (a b x : E) : V a b x = jordanTriple a b x
```

**`ProbabilisticTheory.JordanAlgebra.innerDerivation_sub_right`**, a lemma, [line 462](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Quadratic/Fundamental.lean#L462).

> Difference expansion of the inner derivation in its second defining argument.

```lean
lemma innerDerivation_sub_right (a b c : E) :
    innerDerivation a (b - c) = innerDerivation a b - innerDerivation a c
```

**`ProbabilisticTheory.JordanAlgebra.innerDerivation_mul_left`**, a lemma, [line 470](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Quadratic/Fundamental.lean#L470).

> The inner derivation of a product in its first argument.

```lean
lemma innerDerivation_mul_left (a b q e : E) :
    innerDerivation (a * b) q e = innerDerivation a (b * q) e + innerDerivation b (a * q) e
```

**`ProbabilisticTheory.JordanAlgebra.tripleOperator_comm`**, a lemma, [line 479](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Quadratic/Fundamental.lean#L479).

> `[V_{a,b}, V_{c,d}] = V_{{a,b,c},d} - V_{c,{b,a,d}}`, the fundamental identity of Jordan triple
> systems.

```lean
lemma tripleOperator_comm (a b c d : E) :
    (V a b).comp (V c d) - (V c d).comp (V a b) =
      V (jordanTriple a b c) d - V c (jordanTriple b a d)
```

**`ProbabilisticTheory.JordanAlgebra.tripleOperator_quadRep_step`**, a lemma, [line 700](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Quadratic/Fundamental.lean#L700).

> The triple-operator commutator law specialized to `(x, y, x, z)` and evaluated at `x`.

```lean
lemma tripleOperator_quadRep_step (x y z : E) :
    V x y (U x z) =
      (2 : ℝ) • V x z (U x y) - U x (jordanTriple y x z)
```

**`ProbabilisticTheory.JordanAlgebra.V_quadRep_eq_quadRep_triple`**, a lemma, [line 720](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Quadratic/Fundamental.lean#L720).

> Combining `tripleOperator_quadRep_step` with its own `y ↔ z` companion (and
> `jordanTriple_outer_comm`, which identifies `jordanTriple z x y` with `jordanTriple y x z`)
> eliminates the `V x z (U x y)` cross-term entirely.

```lean
lemma V_quadRep_eq_quadRep_triple (x y z : E) :
    V x y (U x z) = U x (jordanTriple y x z)
```

**`ProbabilisticTheory.JordanAlgebra.quadRep_fundamental_apply`**, a lemma, [line 733](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Quadratic/Fundamental.lean#L733).

> Pointwise form of the fundamental formula for the quadratic representation:
> `U_{U_x y} z = U_x U_y U_x z`.

```lean
lemma quadRep_fundamental_apply (x y z : E) :
    U (U x y) z = U x (U y (U x z))
```

**`ProbabilisticTheory.JordanAlgebra.quadRep_fundamental`**, a lemma, [line 1001](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Quadratic/Fundamental.lean#L1001).

> The fundamental formula for the quadratic representation:
> `U_{U_x y} = U_x ∘ U_y ∘ U_x`.

```lean
lemma quadRep_fundamental (x y : E) :
    U (U x y) = (U x).comp ((U y).comp (U x))
```

**`ProbabilisticTheory.JordanAlgebra.quadRep_fundamental_jpow`**, a lemma, [line 1007](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Quadratic/Fundamental.lean#L1007).

> The fundamental formula on powers of one element.

```lean
lemma quadRep_fundamental_jpow (a : E) (m n k : ℕ) :
    U (U ((a ^[m]) : E) ((a ^[n]) : E)) ((a ^[k]) : E) =
      U ((a ^[m]) : E) (U ((a ^[n]) : E) (U ((a ^[m]) : E) ((a ^[k]) : E)))
```

## Depends on

- [The Jordan triple product](../part-03/quadratic-triple.md)

## Proof depends on

- [Quadratic representations of powers](power-quadratic.md)

## Sources

- [PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Quadratic/Fundamental.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Quadratic/Fundamental.lean)
