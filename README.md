# Models as a Service: 15-minute Theatre Session

## Session Description

The goal is to showcase the variety of models accessible through Azure AI Studio, emphasize their deployment simplicity, and the developer's flexibility to select different models according to requirements without code changes using the Azure AI Model Inference SDKs.

## Learning Outcomes

This workshop demonstrates how to leverage the Azure AI Foundry to deploy models as a service. The session will cover the following topics:

### Azure AI Studio

Azure AI Studio is a platform that enables developers to build, deploy, and manage AI models. It provides a range of pre-trained models that can be deployed as a service, as well as tools for training custom models.

### AI Studio Models as a Service

Azure AI Studio Models as a Service (MaaS) are pre-trained models that can be deployed as a service. They are accessible via REST APIs and SDKs and can be used for a variety of tasks, including text generation, text completion, and text classification.

### Serverless Models

Serverless models are deployed on-demand and are cost-effective. They are ideal for low to moderate usage scenarios. The models are deployed as a service and can be accessed via REST APIs and SDKs. This demo uses serverless models.

### Managed Compute

Managed compute models are deployed on dedicated resources and are ideal for high-usage scenarios. They are more expensive than serverless models but offer better performance and scalability.

### AI Studio Hubs

Azure AI Studio Hubs are the units of organization for models. They are deployed by region, and you can have multiple hubs in a region. The models are deployed by project, and projects are deployed by hub.

## Additional Resources and Continued Learning

If you want to deliver this talk yourself, you can find the [presenter and proctor resources here](./session-delivery-resources/README.md).

| Resources          | Links                             | Description        |
|:-------------------|:----------------------------------|:-------------------|

## Content Owners

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->

<table>
<tr>
    <td align="center"><a href="http://learnanalytics.microsoft.com">
        <img src="https://github.com/gloveboxes.png" width="100px;" alt="Dave Glover"/><br />
        <sub><b>Dave Glover
</b></sub></a><br />
            <a href="https://github.com/gloveboxes" title="talk">📢</a>
    </td>
</tr>
</table>

<!-- ALL-CONTRIBUTORS-LIST:END -->

## Responsible AI

Microsoft is committed to helping our customers use our AI products responsibly, sharing our learnings, and building trust-based partnerships through tools like Transparency Notes and Impact Assessments. Many of these resources can be found at [https://aka.ms/RAI](https://aka.ms/RAI).
Microsoft’s approach to responsible AI is grounded in our AI principles of fairness, reliability and safety, privacy and security, inclusiveness, transparency, and accountability.

Large-scale natural language, image, and speech models - like the ones used in this sample - can potentially behave in ways that are unfair, unreliable, or offensive, in turn causing harms. Please consult the [Azure OpenAI service Transparency note](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) to be informed about risks and limitations.

The recommended approach to mitigating these risks is to include a safety system in your architecture that can detect and prevent harmful behavior. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) provides an independent layer of protection, able to detect harmful user-generated and AI-generated content in applications and services. Azure AI Content Safety includes text and image APIs that allow you to detect material that is harmful. Within Azure AI Studio, the Content Safety service allows you to view, explore and try out sample code for detecting harmful content across different modalities. The following [quickstart documentation](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) guides you through making requests to the service.

Another aspect to take into account is the overall application performance. With multi-modal and multi-models applications, we consider performance to mean that the system performs as you and your users expect, including not generating harmful outputs. It's important to assess the performance of your overall application using [Performance and Quality and Risk and Safety evaluators](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in). You also have the ability to create and evaluate with [custom evaluators](https://learn.microsoft.com/azure/ai-studio/how-to/develop/evaluate-sdk#custom-evaluators).

You can evaluate your AI application in your development environment using the [Azure AI Evaluation SDK](https://microsoft.github.io/promptflow/index.html). Given either a test dataset or a target, your generative AI application generations are quantitatively measured with built-in evaluators or custom evaluators of your choice. To get started with the azure ai evaluation sdk to evaluate your system, you can follow the [quickstart guide](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk). Once you execute an evaluation run, you can [visualize the results in Azure AI Studio](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).
