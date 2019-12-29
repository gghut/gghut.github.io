spring boot test
===

```java
@RunWith(SpringRunner.class)
@SpringBootTest
@Transactional
public class MarketApplicationTests {

    MockMvc mockMvc;

    @Autowired
    WebApplicationContext webApplicationContext;

    @Before
    public void before(){
        mockMvc = MockMvcBuilders.webAppContextSetup(webApplicationContext).build();
    }

    @Test
    public void contextLoads() throws Exception {
        MvcResult result = mockMvc.perform(MockMvcRequestBuilders.get("/merchandise/list").accept(MediaType.APPLICATION_JSON_UTF8)).andReturn();
        int status = result.getResponse().getStatus();
        String context = result.getResponse().getContentAsString();
        Assert.assertEquals("正确返回值为200", 200, status);
        System.out.println(context);
    }


}
```