# GaugeTheory

The folder [Physlib/ClassicalFieldTheory/GaugeTheory/](https://github.com/leanprover-community/physlib/tree/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalFieldTheory/GaugeTheory): 1 module, with an article.

The repository's API map for this folder, *Gauge theory* ([Physlib/ClassicalFieldTheory/GaugeTheory/API-map.md](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalFieldTheory/GaugeTheory/API-map.md)): its Content section, with the sentences it marks as not yet formalized left out (…). A citation \[n\] links the module its n-th Lean reference names.

*Content (Alpha)*

> ### Local formulation
>
> Despite the geometric formulation being global, in practice gauge theories are often described locally. This local formulation is what is commonly used in physics, particularly in the context of electromagnetism and the Standard Model. Here one is much less reliant on certain choices one has to make regarding for example the regularity of the fields associated with the principal bundle.
>
> We first introduce a general concept called *local gauge data*, which abstractly encapsulates all the information needed to describe gauge transformations and gauge fields at a single spacetime point.
>
> #### Local gauge data
>
> If one only cares about local gauge transformations, one can ask what data is needed at a point x. Let G be the gauge group and 𝔤 its Lie algebra. A local Lagrangian sees a gauge transformation only through its action on the fields and finitely many of their derivatives at x, and so only through the Taylor series of the gauge transformation at x. If every smooth function is an allowed gauge transformation, Borel's theorem shows that every Taylor series compatible with G arises, convergent or not. These Taylor series, the jets at x, form a group G\_J, and their infinitesimal counterparts a Lie algebra 𝔤\_J over ℝ.
>
> So at x, a gauge transformation is replaced by its jet U ∈ G\_J, and an infinitesimal gauge transformation by a jet a ∈ 𝔤\_J. The data needed at x is whatever enters the transformation laws. A gauge field A\_μ is Lie algebra valued, and under U it transforms as A\_μ ↦ Ad\_U A\_μ + θ\_μ(U). Here Ad\_U is the adjoint action, U A\_μ U⁻¹ for a matrix group, and θ\_μ(U) = i (∂\_μ U) U⁻¹ is the Maurer–Cartan form, the inhomogeneous term that makes A\_μ a gauge field rather than a matter field. A Lagrangian also involves derivatives of the gauge field, as in the field strength F\_μν = ∂\_μ A\_ν − ∂\_ν A\_μ + ⁅A\_μ, A\_ν⁆ with ⁅A, B⁆ = i (AB − BA), so one needs the spacetime derivatives ∂\_μ of Lie algebra jets, together with multiplication by a coordinate x\_μ to build jets with prescribed derivatives. Finally, a jet can be evaluated at x, giving U(x) ∈ G and a(x) ∈ 𝔤, and a global gauge transformation g ∈ G, or c ∈ 𝔤, gives a constant jet. We define *local gauge data* to be exactly this information: G, 𝔤, G\_J, 𝔤\_J and these operations, subject to the rules that make the transformation laws consistent. Among them are the Leibniz rules ∂\_μ ⁅a, b⁆ = ⁅∂\_μ a, b⁆ + ⁅a, ∂\_μ b⁆ and ∂\_μ (x\_ν a) = x\_ν ∂\_μ a + δ\_μν a; the cocycle law θ\_μ(UV) = θ\_μ(U) + Ad\_U θ\_μ(V), which says that transforming A\_μ by V and then by U is the same as transforming by UV; and ∂\_μ θ\_ν(U) − ∂\_ν θ\_μ(U) + ⁅θ\_μ(U), θ\_ν(U)⁆ = 0, which says that a pure-gauge field has vanishing field strength. [\[9\]](localgaugedata-basic.md)
>
> Every g ∈ G is the value at x of its constant jet, so evaluation G\_J → G is surjective and the inclusion of constants G → G\_J is injective; the same holds for 𝔤\_J → 𝔤 and 𝔤 → 𝔤\_J. [\[10\]](localgaugedata-basic.md) Applied to constant jets, the rules for G\_J and 𝔤\_J show that Ad\_g is a Lie algebra automorphism of 𝔤 for every g ∈ G, and that ∂\_μ commutes with Ad\_g. [\[11\]](localgaugedata-basic.md)
>
> For a multiset s of directions, the iterated derivative ∂\_s applies ∂\_μ once for each μ in s. It satisfies ∂\_(s + t) = ∂\_s ∂\_t and the iterated Leibniz rule ∂\_s ⁅a, b⁆ = Σ ⁅∂\_s₁ a, ∂\_s₂ b⁆, the sum running over the ways of splitting s as s₁ + s₂. If s is non-empty then ∂\_s c = 0 for every constant c ∈ 𝔤, and ∂\_s commutes with Ad\_g for g ∈ G. [\[12\]](localgaugedata-basic.md) The value (∂\_s (x\_μ a))(x) is the number of times μ occurs in s, multiplied by (∂\_(s − μ) a)(x). [\[13\]](localgaugedata-basic.md)
>
> A morphism of local gauge data consists of maps G → G', 𝔤 → 𝔤', G\_J → G'\_J and 𝔤\_J → 𝔤'\_J compatible with all of the operations above. It intertwines Ad on 𝔤 and 𝔤', and commutes with ∂\_s. [\[14\]](localgaugedata-basic.md) Morphisms have identities and compose. [\[15\]](localgaugedata-basic.md) …
>
> #### The abelian theory
>
> In electromagnetism the gauge field is the electromagnetic potential \{1}, a Lorentz-vector-valued field on spacetime, and its field strength is built from that potential. [\[2\]](../../electromagnetism/kinematics/empotential.md)[\[3\]](../../electromagnetism/kinematics/fieldstrength.md) A gauge transformation shifts the potential by the gradient of a scalar \{2}, and the pure-gauge potential is the shift of zero. [\[4\]](../../electromagnetism/kinematics/gaugetransformation.md) Gauge transformations leave the field strength invariant. [\[5\]](../../electromagnetism/kinematics/gaugetransformation.md) In particular a pure-gauge potential has vanishing field strength, and this relies on raising the index of the gradient with the Minkowski metric: the bare gradient of a scalar can have nonzero field strength. [\[6\]](../../electromagnetism/kinematics/gaugetransformation.md) Gauge transformations compose: the trivial shift is the identity and successive shifts add. [\[7\]](../../electromagnetism/kinematics/gaugetransformation.md) They commute with the action of the Lorentz group. [\[8\]](../../electromagnetism/kinematics/gaugetransformation.md)
>
> #### The Standard Model gauge group
>
> The Standard Model gauge group \{3} is SU(3) × SU(2) × U(1), with its projections onto the three factors and a central discrete subgroup of sixth roots of unity. [\[1\]](../../particles/standardmodel/gaugegroup/basic.md)
>
> #### The non-abelian theory
>
> … Progress on this API is tracked in a GitHub issue \{5}.

Its references:

> - \{1\} Electromagnetic Potential API map — [Physlib/Electromagnetism/Kinematics/API-map.md](../../electromagnetism/kinematics/README.md)
> - \{2\} Wikipedia, Mathematical descriptions of the electromagnetic field, Gauge freedom, https://en.wikipedia.org/wiki/Mathematical\_descriptions\_of\_the\_electromagnetic\_field#Gauge\_freedom
> - \{3\} Standard Model gauge group API map — [Physlib/Particles/StandardModel/GaugeGroup/API-map.md](../../particles/standardmodel/gaugegroup/README.md)
> - \{4\} Wikipedia, Gauge theory, https://en.wikipedia.org/wiki/Gauge\_theory
> - \{5\} Physlib GitHub issue #859, https://github.com/leanprover-community/physlib/issues/859

Modules in [LocalGaugeData/](https://github.com/leanprover-community/physlib/tree/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalFieldTheory/GaugeTheory/LocalGaugeData):

- [Local gauge data](localgaugedata-basic.md)
