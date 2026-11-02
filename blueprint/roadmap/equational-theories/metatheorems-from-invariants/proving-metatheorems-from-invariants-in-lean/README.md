# Proving metatheorems from invariants in Lean

For the rest of this chapter we readopt the convention of calling ‘theorem' an important result, not necessarily pertaining to specific equations.

An invariant is generally a *syntactic* property of an expression. However, invariants can also be described and calculated *semantically* through the notion of a *lifting magma family*, described below. The general idea is that the value of an invariant for an expression can be computed by substituting specific values for the variables in the expression and evaluating the result in a certain magma in the lifting magma family; additional requirements ensure that the fundamental property of invariants is satisfied.

- [Lifting Magma Family](lifting-magma-family.md)
- [Evaluation theorem for lifting magma families](lifting-magma-basis-evaluation.md)
- [The fundamental property of invariants](fundamental-property-of-invariants.md)
