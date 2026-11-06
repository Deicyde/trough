# Proving metatheorems from invariants in Lean

For the rest of this chapter we readopt the convention of calling ‘theorem’ an important result, not necessarily pertaining to specific equations.

An invariant is generally a *syntactic* property of an expression. However, invariants can also be described and calculated *semantically* through the notion of a *lifting magma family*, described below. The general idea is that the value of an invariant for an expression can be computed by substituting specific values for the variables in the expression and evaluating the result in a certain magma in the lifting magma family; additional requirements ensure that the fundamental property of invariants is satisfied.

- [Lifting Magma Family](lifting-magma-family.md)

**Example.** The free abelian groups form a lifting magma family. When the underlying set is finite, the groups are isomorphic to $\mathbb{Z}^n$.

**Example.** Lists form a lifting magma family.

The key consequence of the [Lifting Magma Family](lifting-magma-family.md) is that it is significantly easier to check whether an equation is satisfied in a lifting magma family.

- [Evaluation theorem for lifting magma families](lifting-magma-basis-evaluation.md)

**Remark.** The result of evaluating an expression along the function $\iota_X : X \to G_X$ *is* the invariant.

In the case of abelian groups, the result of evaluation is the variables in the expression with multiplicity. In the case of lists, the result of evaluation is the variables in the expression in the order they appear.

When the lifting magma family has good computational properties, calculating the invariant becomes easy.

**Remark.** Given an equation $\phi$ in the language of magmas (possibly involving logical operations other than equality and universal quantification), the initial (i.e., most general) magmas satisfying $\phi$ (provided they exist) form a lifting magma family.

However, for the purpose of generating invariants, we are interested in lifting magma families with convenient descriptions that are computationally tractable.

**Remark.** Suppose $S$ is a finite set of equations in the language of magmas that is a confluent term rewriting system under a certain ordering of the terms (in the sense of the Knuth-Bendix algorithm). Then the initial magmas satisfying $S$ form a lifting magma family where equality of elements in the magma is decidable.

This offers a way of generating examples of lifting magma families with good computational properties for computing invariants of expressions.
